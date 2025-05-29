import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QPushButton, 
                              QFileDialog, QWidget, QLabel)
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt
from PIL import Image, ImageEnhance
import cv2
import numpy as np
import os

class ImageProcessorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Get handwritten text from photo")
        self.setFixedSize(500, 400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.label = QLabel("Select images to process")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        
        self.select_btn = QPushButton("Select Images")
        self.select_btn.clicked.connect(self.select_images)
        layout.addWidget(self.select_btn)
        
        self.process_btn = QPushButton("Convert")
        self.process_btn.setStyleSheet("background-color: green; color: white;")
        self.process_btn.clicked.connect(self.process_images)
        layout.addWidget(self.process_btn)
        
        self.save_btn = QPushButton("Select Output Folder")
        self.save_btn.clicked.connect(self.select_output_folder)
        layout.addWidget(self.save_btn)
        
        self.output_folder = ""
        self.image_paths = []
    
    def select_images(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Images", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if files:
            self.image_paths = files
            self.label.setText(f"Selected {len(files)} images")
    
    def select_output_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder:
            self.output_folder = folder
            self.label.setText(f"Output folder: {folder}")
    
    def process_images(self):
        if not self.image_paths:
            self.label.setText("No images selected!")
            return
        if not self.output_folder:
            self.label.setText("No output folder selected!")
            return
        
        for image_path in self.image_paths:
            try:
                image = Image.open(image_path)
                image.info['dpi'] = (300, 300)
                
                enhancer = ImageEnhance.Contrast(image)
                image_enhanced = enhancer.enhance(2.0)
                
                image_gray = np.array(image_enhanced.convert("L"))
                blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)
                
                adaptive_thresh = cv2.adaptiveThreshold(
                    blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                    cv2.THRESH_BINARY, 15, 10)
                
                kernel = np.ones((2, 2), np.uint8)
                adaptive_thresh = cv2.morphologyEx(adaptive_thresh, cv2.MORPH_OPEN, kernel)
                
                result_image = Image.fromarray(adaptive_thresh)
                filename = os.path.basename(image_path)
                output_path = os.path.join(self.output_folder, f"processed_{filename}")
                result_image.save(output_path, dpi=(300, 300), quality=95)
                
            except Exception as e:
                self.label.setText(f"Error processing {image_path}: {str(e)}")
                return
        
        self.label.setText(f"Successfully processed {len(self.image_paths)} images")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageProcessorApp()
    window.show()
    sys.exit(app.exec())
