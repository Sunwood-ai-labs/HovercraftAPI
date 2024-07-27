from HovercraftAPI import SlideGenerator, SlideCapturer
import os

# スライド生成
generator = SlideGenerator("example/README.md", "output", "mytheme.css")
generator.generate_slides()

# スライドキャプチャ
capturer = SlideCapturer("output")
capturer.capture_slides_as_png()

# 動画生成
image_dir = os.path.join("output", 'slide_images')
capturer.create_video_from_images(image_dir, 'presentation_video.mp4')
