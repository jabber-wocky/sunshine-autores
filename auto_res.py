import sys, subprocess, os

# full_path = os.getcwd()
# f = open(os.path.join(full_path, "log.txt"), "a")

# f.write(f"\n=========\nvars: {sys.argv[1]} x {sys.argv[2]}\n")

MAX_SUNSHINE_CLIENT_WIDTH = 1920
SUNSHINE_CLIENT_WIDTH = int(sys.argv[1])
SUNSHINE_CLIENT_HEIGHT = int(sys.argv[2])
SUNSHINE_CLIENT_RATIO = SUNSHINE_CLIENT_WIDTH / SUNSHINE_CLIENT_HEIGHT

# f.write(f"client resolution: {SUNSHINE_CLIENT_WIDTH} x {SUNSHINE_CLIENT_HEIGHT}\n")

if SUNSHINE_CLIENT_WIDTH > MAX_SUNSHINE_CLIENT_WIDTH:
    SUNSHINE_CLIENT_WIDTH = MAX_SUNSHINE_CLIENT_WIDTH
    SUNSHINE_CLIENT_HEIGHT = int(SUNSHINE_CLIENT_WIDTH / SUNSHINE_CLIENT_RATIO)
    # f.write(f"new resolution: {SUNSHINE_CLIENT_WIDTH} x {SUNSHINE_CLIENT_HEIGHT}\n")


subprocess.run(
    [
        "QRes.exe",
        f"/X:{SUNSHINE_CLIENT_WIDTH}",
        f"/Y:{SUNSHINE_CLIENT_HEIGHT}",
    ]
)
