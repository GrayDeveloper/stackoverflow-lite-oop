class User(object):
    users = []

    def __init__(self, name, email, password, roles):
        self.name = name
        self.email = email
        self.password = password
        self.roles = roles

    def _save(self, user):
        User.users.append(user)
        return dict(
            name=User.users[0].name,
            email=User.users[0].email
        )

    def _update(self, Users):
        updated_user = dict(
            name=Users.get('name'),
            email=Users.get('email')
        )
        User.users.append(updated_user)
        return updated_user


class Admin(User):
    def __init__(self, name, email, password):
        super(Admin, self).__init__(name=name, email=email,
                                    password=password, roles="Admin")
