"""Optional local screenshot preparation; OpenCV is needed only for this tool."""
from pathlib import Path
import sys
import cv2

source = Path(sys.argv[1])
target = Path(sys.argv[2])
target.parent.mkdir(parents=True, exist_ok=True)
im = cv2.imread(str(source))
if im is None:
    raise ValueError("image could not be read")
# Clip editor chrome, OS/taskbar, and HUD containing machine-specific paths.
if not cv2.imwrite(str(target), im[455:895, 50:1435], [cv2.IMWRITE_JPEG_QUALITY, 90]):
    raise RuntimeError("image could not be saved")
