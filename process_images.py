import os
import cv2

def analyze_images(input_dir=".", output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)

    # Find image files in the current directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path)

            if img is None:
                continue

            # Convert to Grayscale & perform Edge Detection
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 100, 200)

            # Save processed image
            save_path = os.path.join(output_dir, f"processed_{filename}")
            cv2.imwrite(save_path, edges)
            print(f"Processed: {filename} -> {save_path}")

if __name__ == "__main__":
    analyze_images()
