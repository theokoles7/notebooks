# Midterm Exam Study Guide
[CSCE-508: Image Processing](../README.md)

**NOTE**: Format of exam consists of multiple-choice, short-answer, true/false, and two simple computation problems.

**NOTE**: This study guide is based on [Lecture 13: Midterm Review](../_lectures_/13_Midterm-Review.pdf).

## Lectures 1-3: Introduction & Fundamentals:
1. Image processing applications (give examples)

    * Detection:
        * Autonomous vehicles rely on sensors and cameras to detect and classify objects like pedestrians, other vehicles, traffic signs, and obstacles.
        * In security and surveillance, object detection identifies and tracks individuals, recognizes suspicious activities, and detects intrusions.
        * Retail stores use object detection to monitor customer behaviour, manage inventory, and prevent theft.

    * Classification: 
        * In the medical field, image classification is used to diagnose diseases and conditions from medical images such as X-rays, MRIs, and CT scans.
        * Facial recognition systems use image classification to identify and verify individuals based on their facial features.
        * Image classification is used in environmental monitoring to analyze satellite and aerial images.

    * Segmentation:
        * Lung lobe segmentation from CT scans
        * Used in monitoring and segmenting inappropriate content from images or videos for social media platforms.
        * Image segmentation methods are used by farmers and agronomists for crop health monitoring, estimating yield and detect plant diseases from images and videos.
        * Image segmentation helps in manufacturing process for quality control, detecting defects in products.

2. What is the relation between image processing & computer vision?

    * High level: Image processing is often a *preprocessing step* in computer vision.

    * Mid level: Image processing provides foundational tools for refining images, while computer vision applies machine learning, pattern recognition, and AI to interpret them.

    * Low level: Many low-level mathematical operations in computer vision (e.g., convolutions in CNNs) originated from traditional image processing.

3. Provide the functions of the two receptors in the retina:

    * Cones: Located in the fovea and are highly sensitive to color

    * Rods: Give a general overall picture of view, are insensitive to color, and are sensitive to low levels of illumination

4. Digital image acquisition:

    * Illumination source:

    * Imaging system: 

    * Projection onto the image plane: 

    * Digitized image: 

    * Sampling vs. Quantization:

        * Sampling is digitizing the coordinate values (usually determined by sensors).

        * Quantization is digitizing the amplitude values.

5. How are 2D images presented?

    A digitial image is a 2D array of pixel values and can be represented as a function $f(x, y)$, where $x$ and $y$ are spatial coordinates, and $f(x, y)$ returns the intensity or gray level of the pixel at that coordinate.

6. Provide the definition and equation(s) for "dynamic range".

    * Dynamic range (or cantrast ratio), is the ratio of the maximum detectable intensity level (saturation) to the minimum detectable intensity level (noise).

    * Methematical definition: $\frac{I_{max}}{I_{min}}$

7. Provide the definition of "spatial resolution".

    Spatial resolution refers to the "smallest discernable details" of a digital image, which is the number of pixels & lines per unit distance. The unit to refer to spatial resolution is DPI (dots per inch).

8. Provide the definition of "intensity resolution".

    Number of intensity levels for each pixel.

9. What are the 3 types adjacency?

    * 4-adjacency: A pixel is adjacent to the ones directly above, below, left, and right (like a "+" shape).

    * 8-adjacency: A pixel is adjacent to all 4-adjacency neighbors + 4 diagonal neighbors (like a square around it).

    * M-adjacency: 

10. In the context of pixel connectivity:

    * What is connected?

    * What is a closed path?

    * What is a connected component?

    * What is a region?