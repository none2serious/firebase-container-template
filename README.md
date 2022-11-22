# firebase-container-template

----
create boilerplate init, to_dict and from_dict functions<br>
given a list of variables. <br>
<br>
e.g.:

``` python
from firebase_container import container_class_from_list as ccl
varlist = "uid firstname lastname email phone".split()
txt = ccl(varlist, class_name="user_class")
print(txt)
```

creates:

``` python
class user_class(object):
    def __init__(
        self,
        uid,
        firstname,
        lastname,
        email,
        phone,
    ):

        self.uid = uid
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone


    def to_dict(self):
        outdict = {
            'uid': self.uid,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'phone': self.phone,
            }

        return(outdict)

    def from_dict(source:dict):
        new_user_class = user_class(
            uid=source['uid'],
            firstname=source['firstname'],
            lastname=source['lastname'],
            email=source['email'],
            phone=source['phone'],
        )

        return(new_user_class)
```
