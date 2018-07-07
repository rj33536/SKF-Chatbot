import re

vulndict={'xss':'xss injection','cross site scripting':'xss injection','malicious script is injected directly':'xss injection',
'Sessions pattern': 'Sessions pattern','unauthenticated access security logs':'Unauthorized and unauthenticated access security logs',
'Unauthorized access security logs':'Unauthorized and unauthenticated access security logs',
'access security logs':'Unauthorized and unauthenticated access security logs',
'Unauthorized and unauthenticated access security logs': 'Unauthorized and unauthenticated access security logs', 
'Disallow the use of old passwords': 'Disallow the use of old passwords','Absolute time out':'Absolute session time out',
'Identify external dependencies': 'Identify external dependencies','session time out':'Absolute session time out',
'Absolute session time out': 'Absolute session time out', 'Incorrect or missing charset': 'Incorrect or missing charset',
'Incorrect or missing charset':'Incorrect charset','missing charset':'Incorrect or missing charset',
'Protecting device memory': 'Protecting device memory','Protect device memory':'Protecting device memory',
'HTTP strict transport security': 'HTTP strict transport security','HTTP transport security':'HTTP strict transport security',
'HTTP security':'HTTP strict transport security','Val,idated cryptographic':'Validated cryptographic modules',
'Validated cryptographic modules': 'Validated cryptographic modules','Block weak passphrases':'Block common password and weak passphrases',
'Block common password and weak passphrases': 'Block common password and weak passphrases',
'Block common password':'Block common password and weak passphrases', 
'Build proccess security hardening': 'Build proccess security hardening','administrative interfaces':'administrative interfaces must not be accessible to untrusted parties', 
'administrative interfaces must not be accessible to untrusted parties': 'administrative interfaces must not be accessible to untrusted parties', 
'OCSP':'OCSP stapling','Insecure communication':'Insecure internal communication',
'OCSP stapling': 'OCSP stapling', 'Client side input validation': 'Client side input validation', 
'Insecure internal communication': 'Insecure internal communication', 
'Certificate paths':'Certificate paths revocation information',
'Certificate paths revocation information': 'Certificate paths revocation information', 
'sanitise sensitive data rapidly from memory': 'sanitise sensitive data rapidly from memory', 
'access control decisions':'Logging access control decisions',
'Logging access control decisions': 'Logging access control decisions', 
'Unauthorised access':'Unauthorised access and modification',
'Unauthorised access and modification': 'Unauthorised access and modification',
'memory dumping attacks':'Mitigate memory dumping attacks',
'Mitigate dumping attacks':'Mitigate memory dumping attacks',
'Mitigate memory dumping attacks': 'Mitigate memory dumping attacks',
'All access controls must fail securely': 'All access controls must fail securely',
'application level logging':'Single application level logging',
'Single application level logging': 'Single application level logging', 
'Include anti': 'Include anti', 'Filename injection':'Filename injection Path traversel',
'Path traversel':'Filename injection Path traversel','File inclusion':'File inclusion attack',
'Filename injection Path traversel': 'Filename injection Path traversel',
'File inclusion attack': 'File inclusion attack', 'deploy in a secure fashion':'Build and deploy in a secure fashion',
'Build in a secure fashion':'Build and deploy in a secure fashion',
'Build and deploy in a secure fashion': 'Build and deploy in a secure fashion',
'Input rejection': 'Input rejection', 
'Identify and use only require functions if using components': 'Identify and use only require functions if using components',
'Transport Security header':'Include Strict Transport Security header',
'Include Strict Transport Security header': 'Include Strict Transport Security header',
'WYSIWYG editors': 'WYSIWYG editors','Differential attack':'Differential analysis attack',
'Differential analysis attack': 'Differential analysis attack', 'Input validation': 'Input validation',
'Domain cookies':'Session Domain cookies','Enforce sensitive information':'Enforce sensitive information to be stored encrypted on device',
'Session Domain cookies': 'Session Domain cookies',
'Data from untrusted sources': 'Data from untrusted sources',
'Enforce sensitive information to be stored encrypted on device': 'Enforce sensitive information to be stored encrypted on device',
'Limiting user input size': 'Limiting user input size','Limiting input size':'Limiting user input size', 
'Canonicalized input':'Canonicalized user input',
'Canonicalized user input': 'Canonicalized user input','step up authentication':'step up or adaptive authentication',
'adaptive authentication':'step up or adaptive authentication', 
'step up or adaptive authentication': 'step up or adaptive authentication', 
'IP adresses in internal HTTP headers': 'IP adresses in internal HTTP headers','LDAP':'LDAP injection',
'Logging guidelines to access sensitive information': 'Logging guidelines to access sensitive information', 
'LDAP injection': 'LDAP injection','Log viewing software':'Log viewing software code injection', 
'Log viewing software code injection': 'Log viewing software code injection',
'No shared knowledge for secret questions': 'No shared knowledge for secret questions', 
'Verbose error':'Verbose error messaging','Verbose error message':'Verbose error messaging',
'Verbose error messaging': 'Verbose error messaging', 'Segregated components': 'Segregated components',
'File inclusion attack II': 'File inclusion attack II',
'Predictable password and or token generation': 'Predictable password and or token generation',
'Log injection': 'Log injection', 'TLS implementation':'TLS implementation must operate in an approved mode of operation',
'TLS implementation must operate in an approved mode of operation': 'TLS implementation must operate in an approved mode of operation',
'Third party components': 'Third party components', 'File upload outside document root': 'File upload outside document root', 
'Verify application is not vulnerable for known security issues': 'Verify application is not vulnerable for known security issues', 
'Display concurrent and active sessions': 'Display concurrent and active sessions', 
'Principle of least privilege': 'Principle of least privilege', 'Enforce policys for sensitive data processing': 'Enforce policys for sensitive data processing',
'Secrets should be secure random generated': 'Secrets should be secure random generated', 
'Access to any master secret must be protected from unauthorized access': 'Access to any master secret must be protected from unauthorized access', 
'centralized security controls': 'centralized security controls',
'Password change leads to destroying concurrent sessions': 'Password change leads to destroying concurrent sessions',
'Unauthorized credential changes': 'Unauthorized credential changes', 
'Available log analysis tools': 'Available log analysis tools', 
'Access control failure': 'Access control failure',
'Sensitive information transmitted by unencrypted methods': 'Sensitive information transmitted by unencrypted methods', 
'XML injection': 'XML injection', 'TLS implementation': 'TLS implementation', 'CA certificates': 'CA certificates', 
'All time sources should be synchronized': 'All time sources should be synchronized', 
'Runtime environment': 'Runtime environment', 'xss injection': 'xss injection', 
'sensitive information stored in cookies': 'sensitive information stored in cookies', 
'Possible attackers of the application must be documented': 'Possible attackers of the application must be documented', 
'Accessible non parsed dynamic scripts': 'Accessible non parsed dynamic scripts', 
'Include X Content Type Options header': 'Include X Content Type Options header', 
'Include anti clickjacking headers': 'Include anti clickjacking headers', 
'Enforce sequential step order': 'Enforce sequential step order', 
'All connections should be TLS': 'All connections should be TLS', 'Debug enabeling': 'Debug enabeling', 
'Screen scraping data harvest': 'Screen scraping data harvest', 
'GET POST requests': 'GET POST requests', 
'Logging guidelines': 'Logging guidelines', 'Cross origin resource sharing': 'Cross origin resource sharing', 
'Character encoding': 'Character encoding', 'External DTD parsing': 'External DTD parsing',
'Error handling on trusted devices': 'Error handling on trusted devices', 
'HTML injections': 'HTML injections', 
'Authentication at a central location': 'Authentication at a central location', 
'The crossdomain xml should only contains trusted domains': 'The crossdomain xml should only contains trusted domains', 
'Forget password functions': 'Forget password functions', 'File': 'File', 'Log rotation and seperation': 
'Log rotation and seperation', 'concurrent session handling': 'concurrent session handling', 
'two factor authentication against username password disclosure': 'two factor authentication against username password disclosure', 
'Log TLS connection failures': 'Log TLS connection failures', 'Sandboxing malicious code': 'Sandboxing malicious code',
'Version management': 'Version management', 'Trusted repositories': 'Trusted repositories', 
'High value transactions': 'High value transactions',
'Sandboxing code':'Sandboxing malicious code',
'logging is performed before executing the transaction': 'logging is performed before executing the transaction',
'Safe javascript jquery methods': 'Safe javascript jquery methods',
'SQL injection':'SQL injection Column truncation', 
'SQL injection Column truncation': 'SQL injection Column truncation',
'Account lockout': 'Account lockout', 'XSLT':'XSLT injections',
'Intrusion detection':'Intrusion detecting and reporting',
'Intrusion detecting and reporting': 'Intrusion detecting and reporting', 'XSLT injections': 'XSLT injections', 
'Signed application components': 'Signed application components', 
'HTTP headers added by a frontend': 'HTTP headers added by a frontend',
'Servers must not be trusted without explicit authentication': 'Servers must not be trusted without explicit authentication',
'Approved random number generator': 'Approved random number generator', 'Repudiation attack': 'Repudiation attack', 
'Password forget pattern': 'Password forget pattern','Repudiation':'Repudiation attack',
'public key pinning':'TLS certificate public key pinning',
'TLS certificate':'TLS certificate public key pinning', 
'TLS certificate public key pinning': 'TLS certificate public key pinning', 
'Content type headers': 'Content type headers','Content type':'Content type headers',
'Session cookies without the HttpOnly flag': 'Session cookies without the HttpOnly flag', 
'Commonly chosen weak passwords and passphrases': 'Commonly chosen weak passwords and passphrases', 
'Commonly chosen passphrases':'Commonly chosen weak passwords and passphrases',
'Commonly chosen weak passwords':'Commonly chosen weak passwords and passphrases',
'Authentication based on the knowledge of a secret URL': 'Authentication based on the knowledge of a secret URL',
'RFD and file download injections': 'RFD and file download injections',
'file download injections':'RFD and file download injections',
'RFD injections':'RFD and file download injections',
'RFD and file download':'RFD and file download injections',
'The audit log must include a priority system': 'The audit log must include a priority system',
'External session hijacking': 'External session hijacking',
'session hijacking':'External session hijacking', 
'HTTP header injection': 'HTTP header injection', 'HTTP header':'HTTP header injection',
'Password leakage': 'Password leakage', 
'Include X XSS': 'Include X XSS','X XSS':'Include X XSS', 
'User registration pattern':'User registration pattern',
'User registration pattern': 'User registration pattern',
'Security settings in your development frameworks': 'Security settings in your development frameworks', 
'Extraneous files in document root': 'Extraneous files in document root',
'Extraneous files in root':'Extraneous files in document root',
'unencrypted links':'HTTPS and weakly or unencrypted links',
'HTTPS and weakly or unencrypted links': 'HTTPS and weakly or unencrypted links', 
'Policy for managing cryptographic keys': 'Policy for managing cryptographic keys', 
'data controller display layer separation': 'data controller display layer separation', 
'Parsing JSON with Javascript': 'Parsing JSON with Javascript',
'Regular expression': 'Regular expression injection', 
'Threat modeling': 'Threat modeling', 'Privilege escalation': 'Privilege escalation',
'Regular expression injection': 'Regular expression injection','SSI':'SSI injections',
'verbose authentication': 'Too verbose authentication', 
'SSI injections': 'SSI injections', 'Too verbose authentication': 'Too verbose authentication',
 'Malicious intent': 'Malicious intent', 
 'Validate the integrity of all security relevant configurations': 'Validate the integrity of all security relevant configurations', 
 'The login functionality should always generate a new session id': 'The login functionality should always generate a new session id', 
 'Audit logs': 'Audit logs', 'SOAP basic profile': 'SOAP basic profile',
 'identify all application components': 'identify all application components',
 'Insecure transmission of cookies':'Insecure transmission of session cookies',
 'Insecure transmission of session cookies': 'Insecure transmission of session cookies',
 'Policy for processing sensitive data': 'Policy for processing sensitive data', 
 'Enforce anti': 'Enforce anti', 'Sandboxing': 'Sandboxing', 
 'information is not stored server side':'Session information is not stored server side',
 'User generated session ids should be rejected by the server': 'User generated session ids should be rejected by the server',
 'Session information is not stored server side': 'Session information is not stored server side', 
'JSON XML':'JSON XML schema','Resource identifier':'Resource identifier injection',
 'JSON XML schema': 'JSON XML schema', 'Resource identifier injection': 'Resource identifier injection',
 'Access management': 'Access management', 'Principle of complete mediation': 'Principle of complete mediation',
 'The possible risks to the application must be documented': 'The possible risks to the application must be documented', 
 'Session ids should be generated with sufficient entropy': 'Session ids should be generated with sufficient entropy', 
'File upload':'File upload injections',
 'File upload injections': 'File upload injections', 'Client side constraints': 'Client side constraints',
 'Application assets hosted on secure location': 'Application assets hosted on secure location', 'Context sensitive authorization': 'Context sensitive authorization', 
 'Proces high value business logic flows in a trusted environment': 'Proces high value business logic flows in a trusted environment',
 'Identifier based authorization': 'Identifier based authorization', 'CSRF on REST': 'CSRF on REST', 'User credentials in audit logs': 'User credentials in audit logs', 
 'HTML Caching and client side caching': 'HTML Caching and client side caching',
 'HTML Caching':'HTML Caching and client side caching',
 'client side caching':'HTML Caching and client side caching', 
 'User restriction for sensitive data': 'User restriction for sensitive data', 
 'Prepared statements and query parameterization': 'Prepared statements and query parameterization', 
 'Authentication enforced by the web sever': 'Authentication enforced by the web sever', 
 'Identifier based':'Identifier based authorization',
 'STRIDE': 'STRIDE', 'Identify all components': 'Identify all components', 'Aggregate access control protection': 'Aggregate access control protection', 'Re authentication': 'Re authentication', 'Does The application enforce the use of secure passwords': 'Does The application enforce the use of secure passwords', 'Command injection': 'Command injection', 'Sensitive information stored alongside the source code': 'Sensitive information stored alongside the source code', 'Client side storage': 'Client side storage', 'Open forward and Open redirects': 'Open forward and Open redirects', 'Are all passwords hashed, salted and stretched': 'Are all passwords hashed, salted and stretched', 'Forward secrecy ciphers': 'Forward secrecy ciphers', 'Aggregate user requests': 'Aggregate user requests', 'Do not support untrusted client side technologies': 'Do not support untrusted client side technologies', 'Hardware key vault': 'Hardware key vault', 'All authentication controls must fail securely': 'All authentication controls must fail securely', 'Client side state management': 'Client side state management',
'X Path':'X Path injections', 'X Path injections': 'X Path injections', 'HSTS preload': 'HSTS preload', 'cross subdomain cookie attack': 'cross subdomain cookie attack', 'Signed message payloads': 'Signed message payloads', 'Sanitize unstructured data': 'Sanitize unstructured data', 'Denial of service by locking out accounts': 'Denial of service by locking out accounts', 'Zero keys and secrets before destroying them': 'Zero keys and secrets before destroying them', 'Unnecessary features enabled or installed': 'Unnecessary features enabled or installed', 'XML attacks': 'XML attacks', 'The logout functionality should revoke the complete session': 'The logout functionality should revoke the complete session', 'Content security policy headers': 'Content security policy headers', 'Double decoding of headers parameters': 'Double decoding of headers parameters', 'Automatic parameter binding': 'Automatic parameter binding', 'Logging implemented on the serverside': 'Logging implemented on the serverside', 'Sending data parameters to untrusted devices': 'Sending data parameters to untrusted devices', 'Submit forms pattern': 'Submit forms pattern', 'Username enumeration': 'Username enumeration', 'proven authentication mechanisms': 'proven authentication mechanisms', 'Enforce random numbers are created with proper entropy at runtime': 'Enforce random numbers are created with proper entropy at runtime', 'Directory listing': 'Directory listing', 'Brute force password guessing': 'Brute force password guessing', 'Client side authentication': 'Client side authentication', 'Encrypt sensitive information different depending on context': 'Encrypt sensitive information different depending on context', 'Single input validation controls': 'Single input validation controls', 'Protection against different exfiltration techniques': 'Protection against different exfiltration techniques', 'Prevent password pre filling': 'Prevent password pre filling', 'Access control pattern': 'Access control pattern', 'Distinguish log': 'Distinguish log', 'not available item': 'not available item', 'Cross site request forgery': 'Cross site request forgery', 'cryptographic function implementation': 'cryptographic function implementation', 'Deny access from remote resources or systems': 'Deny access from remote resources or systems', 'Keys and passwords should be replaceable': 'Keys and passwords should be replaceable', 'Logging validation failures': 'Logging validation failures', 'Automated spamming via feedback scripts': 'Automated spamming via feedback scripts', 'cryptographic modules must fail securely': 'cryptographic modules must fail securely', 'Parsing data  exchange formats': 'Parsing data  exchange formats', 'Positive validation model': 'Positive validation model', 'Server side validation': 'Server side validation', 'Server side request forgery': 'Server side request forgery', 'API resonses security headers': 'API resonses security headers', 'Session cookies without the Secure flag': 'Session cookies without the Secure flag', 'Integrity check and authorised modification': 'Integrity check and authorised modification', 'Protect agains exported activities or content providers': 'Protect agains exported activities or content providers', 'Strong CRYPTO through CA hierachy': 'Strong CRYPTO through CA hierachy', 'Centralized the mechanisms for protecting resources and the access': 'Centralized the mechanisms for protecting resources and the access', 'TLS settings are in line with current leading practice': 'TLS settings are in line with current leading practice', 'XXE injections': 'XXE injections', 'Communication between components (low privileges)': 'Communication between components (low privileges)', 'File upload anti virus check': 'File upload anti virus check', 'Data retention policy': 'Data retention policy', 'PII protection': 'PII protection', 'High level architecture should be defined': 'High level architecture should be defined', 'Robots.txt': 'Robots.txt', 'Protect sensitive activities intents or content providers': 'Protect sensitive activities intents or content providers', 'Avoid the use of default and predictable acounts.': 'Avoid the use of default and predictable acounts.', 'Verbose version information': 'Verbose version information', 'Verify integrity using checksums': 'Verify integrity using checksums', 'Unproven cryptographic algorithms': 'Unproven cryptographic algorithms', 'Verify that structured data is strongly typed and validated': 'Verify that structured data is strongly typed and validated', 'Session IDs do not timeout (idl)': 'Session IDs do not timeout (idl)', 'Disable autocomplete for all the input fields in forms': 'Disable autocomplete for all the input fields in forms', 'authenticated data cleared from client storage': 'authenticated data cleared from client storage', 'Verify that the session id is never disclosed': 'Verify that the session id is never disclosed', 'Ensure overall security': 'Ensure overall security', 'Dynamic scripting injection': 'Dynamic scripting injection', 'Insecure datastorage': 'Insecure datastorage', 'Logout structuring': 'Logout structuring', 'Cryptographic modules should operate in their approved mode according to their published security policies': 'Cryptographic modules should operate in their approved mode according to their published security policies', 'Auto escaping technology': 'Auto escaping technology', 'Session management control': 'Session management control', 'Sensitive information in code or online repositories': 'Sensitive information inx code or online repositories', 'Generate strong crypto tokens with at least 120 bit of effective entropy': 'Generate strong crypto tokens with at least 120 bit of effective entropy', 
'HTTP request': 'HTTP request methods',
'HTTP request methods': 'HTTP request methods'}
vulndict =  {k.lower(): v for k, v in vulndict.items()}


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def entity_recognizer(sentence):
    listofWords = re.findall(r"[\w']+|[.,!?;]", sentence)
    copyofWords=[]
    customentitiesDict = {}
    for l in listofWords:
        copyofWords.append(l)
    originalpos3 =[]
#trigram
    i=-1
    j=-1
    while(i<len(listofWords)):
        i=i+1
        j=j+1
        originalpos3.append(i)
        if (i <len(listofWords)-2):
            s3 = listofWords[i]+' '+listofWords[i+1]+' '+listofWords[i+2]
            if (s3 in vulndict.keys()):

                originalpos3.pop()
                customentitiesDict[i,i+1,i+2] = s3
                copyofWords[j:j+3] = [vulndict[s3]]
                i=i+2
                originalpos3.append(i)
  
    #print(originalpos3)
    #print(copyofWords)
    #print(customentitiesDict)
#bigram
    i=-1
    j=-1
    copyofWords2  =[]
    originalpos2 = []
    for w in copyofWords:
        copyofWords2.append(w)
    while(i<len(copyofWords)):
        i=i+1
        j=j+1
        originalpos2.append(originalpos3[i])
        if i<len(copyofWords)-1:
            s2 = copyofWords[i]+' '+copyofWords[i+1]
            if s2 in vulndict.keys():
                originalpos2.pop()
                customentitiesDict[originalpos3[i],originalpos3[i+1]] = s2
                copyofWords2[j:j+2] = [vulndict[s2]]
                i=i+1
                originalpos2.append(originalpos3[i])
                
    #print(originalpos2)
    #print(copyofWords2)
    #print(customentitiesDict)
    i=0
#unigram
    #if not copyofWords2:
     #   for l in listofWords:
      #      copyofWords2.apppend(l)
       # print ("yes")
            
    while (i<len(copyofWords2)):
        
        if copyofWords2[i] in vulndict.keys():
            customentitiesDict[originalpos2[i]]= copyofWords2[i]
            copyofWords2[i] = vulndict[copyofWords2[i]]
        i=i+1
            
                
    #print(originalpos2)
    #print(copyofWords2)
    #print(customentitiesDict)
    for x in customentitiesDict:
        y=customentitiesDict[x]
    
        if y=="":
           return None
        else:
           return vulndict[y]
        
    #while()
            
        
        
#sent = input("enter text")
#print(entity_recognizer(sent.lower()))
