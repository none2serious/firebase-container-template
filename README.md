# firebase-container-template

----
In Google's Firebase docs, they describe an idiomatic way to integrate python classes with firebase. You create __init__, to_dict, and from_dict functions that handle populating and storing data from a [python class](https://firebase.google.com/docs/firestore/query-data/get-data), which is then available to use with the rest of your class functions.<br>
<br>
It works really well. But manually constructing and maintaining the init/to/from variables is repetitive and error prone.<br>
This script creates appropriate boilerplate init, to_dict, and from_dict functions given a list of variable names. <br>

``` python
 container_class_from_list(varlist,
                            class_name="myclass",
                            save_dir=None,
                            usetabs=False,
                            num_spaces=4.
                            ):

```
<br>
e.g.:

``` python
from firebase_container import container_class_from_list as ccfl
varlist = "uid username email subscriptions use_history".split()
usr_class_txt = cclf(varlist, class_name="user_class", savedir='/projects/secret')
print(usr_class_txt)
```

yeilds the text below, using 4 spaces per indentation level (not tabs) and saves it in '/projects/secret/user_class.py'<br>
You can then add your own logic and operations. See link above for details about instantiating the object from, and saving the data to, a firebase db object <br>

``` python
class user_class(object):
    def __init__(
        self,
        uid,
        username,
        email,
        subscriptions,
        use_history,
    ):

        self.uid = uid
        self.username = username
        self.email = email
        self.subscriptions = subscriptions
        self.use_history = use_history


    def to_dict(self):
        outdict = {
            'uid': self.uid,
            'username': self.username,
            'email': self.email,
            'subscriptions': self.subscriptions,
            'use_history': self.use_history,
            }

        return(outdict)

    def from_dict(source:dict):
        new_user_class = user_class(
            uid=source['uid'],
            username=source['username'],
            email=source['email'],
            subscriptions=source['subscriptions'],
            use_history=source['use_history'],
        )

        return(new_user_class)
```
