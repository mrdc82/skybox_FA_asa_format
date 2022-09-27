**Skybox Firewall Assurance Shadow Rule Removal**

The purpose of this script, is to take an output of shadow rules from Skybox into a csv file, and format the file to an ASA standard.

With that, the file can be used to remove shadowed rules.
For our purpose in our environment, we dont have the change manager module, but we do have a script which will output shadow rules on a daily basis.

**See git repo, "shadow rule daily checks"**

From there, we can use our orchestrator to run a rule removal script.

Your text output will be different compared to ours, as this is the standard we use. 

**Dont forget to install requirements**
_pip install -r requirements.txt_

Python Version **3.10.7**