# The volume of a sphere with radius r is 4/3 π r3. What is the volume of a sphere with radius 5?
import math
r = 5
print('Answer One')
print(4/3*math.pi*r**3)

# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?

price = 24.95
discount = .6
copies = 60
print('Answer Two')
print(3+1*price*discount+(copies-1)*price*discount+.75*(copies-1))


# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
start_time = 6*60+52
easy_pace = 8.15
hard_pace = 7.12

end_time = start_time+easy_pace*2+hard_pace

print(str(int(end_time//60))+':' +str(int(end_time % 60)))

