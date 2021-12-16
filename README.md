### Log4J_Version_Checker
---

This tool will search the directory that you provide as an argument for all files that begin with `log4j` and end with `jar`. Once identified the tool will then extract the `manifest.mf` file from the JAR and parse it for the version of the package. Below is the required syntax to use the tool:
`python Log4J_Version_Checker.py <Directory_To_Search>`

This tool was created in response to [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) to help my organization identify machines that had affected Log4J pacakages. If you identify packages which are vulnerable to the referenced it's important that you follow the recommended patching/mitigation strategies as this vulnerability allows for Remote Code Execution. For more information you can reference the [CISA Website](https://www.cisa.gov/uscert/apache-log4j-vulnerability-guidance) which has a wealth of information including important links.
