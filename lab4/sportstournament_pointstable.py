points = [45, 60, -10, 75, 30, 55]

points = [p if p >= 0 else 0 for p in points]

points.sort(reverse=True)

winner = points[0]
runner_up = points[1]

print("Winner Points:", winner)
print("Runner-up Points:", runner_up)
print("Leaderboard:", points)