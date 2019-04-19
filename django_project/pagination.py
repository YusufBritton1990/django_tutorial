from django.core.paginator import Paginator

posts = ['1','2','3','4','5']

# this will show two post at a time on the page
p = Paginator(posts, 2)

print(p.num_pages) #return 3 pages

#using page_range will make an interable
for page in p.page_range:
    print("page " + str(page)) # return 1,2,3. these are the page numbers

p1 = p.page(1)
print(p1) #return Page 1 of 3
print(p1.number) #return 1
print(p1.object_list) #return list ['1', '2'], showing objects on a page

# Checking to see if there is a prior page
print(p1.has_previous())

# Checking to see if there is a prior page
print(p1.has_next())
print(p1.next_page_number())
