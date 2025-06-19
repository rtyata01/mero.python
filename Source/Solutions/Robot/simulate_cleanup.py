class Robot:
    def __init__(self, room, start):
        self.room = room
        self.pos = start
        self.d = 0  # facing up: 0=up,1=right,2=down,3=left
        self.cleaned = set()
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

    def move(self):
        x, y = self.pos
        dx, dy = self.dirs[self.d]
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(self.room) and 0 <= new_y < len(self.room[0]) and self.room[new_x][new_y] == 1:
            self.pos = (new_x, new_y)
            return True
        return False

    def turnLeft(self):
        self.d = (self.d - 1) % 4

    def turnRight(self):
        self.d = (self.d + 1) % 4

    def clean(self):
        self.cleaned.add(self.pos)

def cleanRoom(robot):
    visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

    def go_back():
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()

    def dfs(x, y, d):
        robot.clean()
        visited.add((x, y))

        for i in range(4):
            new_d = (d + i) % 4
            dx, dy = directions[new_d]
            new_x, new_y = x + dx, y + dy

            if (new_x, new_y) not in visited and robot.move():
                dfs(new_x, new_y, new_d)
                go_back()
            robot.turnRight()

    dfs(0, 0, 0)

# Simulated room and robot
room = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 0]
]

start = (1, 0) # Robot starts at (1, 0), facing up (direction = 0)
robot = Robot(room, start)
cleanRoom(robot)

print("Cleaned cells:", robot.cleaned)
