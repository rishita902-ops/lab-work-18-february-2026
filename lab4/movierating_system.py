ratings = [5, 4, 3, 6, 2, 5, 0, 4]

ratings = [r for r in ratings if 1 <= r <= 5]

average = sum(ratings) / len(ratings)
five_star = ratings.count(5)

ratings.sort()

print("Average Rating:", average)
print("5-Star Ratings:", five_star)
print("Sorted Ratings:", ratings)