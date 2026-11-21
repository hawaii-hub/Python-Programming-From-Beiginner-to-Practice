from admin import Admin,Privileges

admin = Admin('liu', 'jingrui', '20', 'yuncheng senior school',
              'can add post', 'can delete post', 'can ban post') 

admin.descibe_user()
admin.show_privileges()
