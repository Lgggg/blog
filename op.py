==================================【6】==================================
#(M)VC_models 的关系(one to many)
=========【manager shell】=========
from uuid import uuid4
user = User(id=str(uuid4()), username='jmilkfan', password='fanguiju')
db.session.add(user)
db.session.commit()
user.posts

user.posts.all()
post_one = Post('First Post')
post_one.id = str(uuid4())
post_one.user_id = user.id
db.session.add(post_one)
db.session.commit()
user.posts.all()
user = db.session.query(User).first()
user.id
post_second = Post('Second Post')
post_second.id = str(uuid4())
post_second.users
post_second.users = user
db.session.add(post_second)
db.session.commit()


==================================【7】==================================
#(M)VC_models 的关系(many to many)
=========【manager shell】=========
from uuid import uuid4
posts = db.session.query(Post).all()
posts
post_one = posts[1]
post_two = posts[0]
from uuid import uuid4
tag_one = Tag('JmilkFan')
tag_one.id = str(uuid4())
tag_two = Tag('FanGuiju')
tag_two.id = str(uuid4())
tag_three = Tag('Flask')
tag_three.id = str(uuid4())
post_one.tags
post_one.tags = [tag_two]
post_two.tags = [tag_one, tag_two, tag_three]
db.session.add(post_one)
db.session.add(post_two)
db.session.commit()

tag_one.posts.all()
tag_one.posts.append(post_one)
tag_one.posts.all()
post_one.tags
#A+B | A.B->list| B.A->AppenderBaseQuery
db.session.add(tag_one)
db.session.commit()

db.session.query(Post).filter_by(title='First Post').first().tags
db.session.query(Tag).filter_by(name='JmilkFan').first().posts.all()


==================================【8】==================================
#(M)VC_models 的关系(many to many)
=========【pip】=========
pip install Flask-Migrate
pip freeze > requirements.txt

