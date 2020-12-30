'''
# Shell Session 1
python manage.py shell

'''

from tags.models import Tag
Tag.objects.all()
# QuerySet [<Tag: shirt>, <Tag: red>, <Tag: Blue>, <Tag: super-computer>, <Tag: clothes>]>
Tag.objects.last()
# <Tag: clothes>
cloth = Tag.objects.last()
cloth.title
# 'clothes'
cloth.slug
# 'clothes'
cloth.products
'''
return 
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x0000028A758E37C0>
'''
cloth.products.all()

# <ProductQuerySet [<Product: T-Shirt>, <Product: Hat>]>

tshirt = cloth.products.first()
tshirt.title
# 'T-Shirt'
tshirt.description
# 'This is an awesome shirts, But it :)'
exit()

'''
# Shell Session 2
python manage.py shell

'''

from products.models import Product
Product.objects.all()

#<ProductQuerySet [<Product: T-Shirt>, <Product: Hat>, <Product: Super Computer>]>

computer = Product.objects.last()
computer.title
# 'Super Computer'

computer.description
# 'Yeah, Big Computer OMG'
computer.slug
# 'super-computer'
computer.timestamp
# datetime.datetime(2020, 11, 2, 7, 15, 22, 301915, tzinfo=<UTC>)
computer.tag
# Raise an error beacuse the Product models doesn't have a field 'tag'

computer.tags
# Raise an error beacuse the Product models doesn't have a field 'tags'
computer.tag_set
# This work beacuse the Tag model has the 'products' field with ManyToMany to Product 
#<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x000002073021CEB0>
computer.tag_set.all()
# Returns an actual QuerySet of the Tag model related to the Product 
#<QuerySet [<Tag: super-computer>]>
>>> exit()
