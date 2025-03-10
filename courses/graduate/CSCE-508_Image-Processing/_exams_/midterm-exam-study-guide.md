# Midterm Exam Study Guide
[CSCE-508: Image Processing](../README.md)

**NOTE**: Format of exam consists of multiple-choice, short-answer, true/false, and two simple computation problems.

**NOTE**: This study guide is based on [Lecture 13: Midterm Review](../_lectures_/13_Midterm-Review.pdf).

## Lecture 1: [Introduction](../_lectures_/01_Introduction.pdf)
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

## Lecture 3: [Digital Image Fundamentals](../_lectures_/03_Digital-Image-Fundamentals.pdf)

1. Provide the functions of the two receptors in the retina:

    * Cones: Located in the fovea and are highly sensitive to color

    * Rods: Give a general overall picture of view, are insensitive to color, and are sensitive to low levels of illumination

2 Digital image acquisition:

    * Illumination source:

    * Imaging system: 

    * Projection onto the image plane: 

    * Digitized image: 

    * Sampling vs. Quantization:

        * Sampling is digitizing the coordinate values (usually determined by sensors).

        * Quantization is digitizing the amplitude values.

3. How are 2D images presented?

    A digitial image is a 2D array of pixel values and can be represented as a function $f(x, y)$, where $x$ and $y$ are spatial coordinates, and $f(x, y)$ returns the intensity or gray level of the pixel at that coordinate.

4. Provide the definition and equation(s) for "dynamic range".

    * Dynamic range (or cantrast ratio), is the ratio of the maximum detectable intensity level (saturation) to the minimum detectable intensity level (noise).

    * Methematical definition: $\frac{I_{max}}{I_{min}}$

5. Provide the definition of "spatial resolution".

    Spatial resolution refers to the "smallest discernable details" of a digital image, which is the number of pixels & lines per unit distance. The unit to refer to spatial resolution is DPI (dots per inch).

6. Provide the definition of "intensity resolution".

    Number of intensity levels for each pixel.

7. What are the 3 types adjacency?

    * 4-adjacency: A pixel is adjacent to the ones directly above, below, left, and right (like a "+" shape).

    * 8-adjacency: A pixel is adjacent to all 4-adjacency neighbors + 4 diagonal neighbors (like a square around it).

    * M-adjacency: Mix of 4- & 8- adjacency, such that if two pixels are connected by an angle, they will not be connected by the diagonal. This eliminates ambiguity in connectivity paths. ([Visual example](https://i.ytimg.com/vi/MuQUXPoxPXk/maxresdefault.jpg))

8. In the context of pixel connectivity:

    "Connectivity" of pixels refers to a path between pixels, represented as a sequence $S$ of distinct and adjacent pixels with coodinates.

    * What is connected?

        Pixels $p$ and $q$ are "connected" if there is a path from $p$ to $q$ in $S$.

    * What is a closed path?

        Connectivity paths in which the starting point is the same as the ending point.

    * What is a connected component?

        All of the pixels in $S$ are connected to pixel $p$.

    * What is a connected set?

        $S$ has only one connected component.

    * What is a region?

        $R$ is a region if $R$ is a connected set.

9. What are inner and outer boundaries?

    * Inner boundary: Set of pixels which have at least on neighbor within the background

    * Outer boundary: The boundary of pixels in the background.

10. Give brief definitions of each of the following distance measures:

    * Euclidean distance: $D_e(p, q) = \sqrt{(x - s)^2 + (y - t)^2}$ (straight-line distance)

    * City-block (D4) distance: $D_4(p, q)  = |x - s| + |y - t|$ (Manhattan or taxi-cab distance)

    * Chessboard (D8) distance (Chebyshev): $D_8(p, q) = max(|x - s|, |y - t|)$

11. Explain the following image operations:

    * Image average: Noise reduction

    * Image subtraction: Enhance difference or change detection

    * Image multiplication: Brightnhess and masking

    * Image division: Normalization and contrast adjustment

## Lecture 4: [Intensity Transformation](../_lectures_/04_Intensity-Transformation.pdf)

1. Compare pixel-level vs. patch-level processing.

    * Pixel-level: Same function is applied to each individiual pixel

    * Patch-level: The same *filter* is applied to sub-regions/patches of the image

2. What is the logistic function used in thresholding?

    The logistic function is a smooth, S-shaped (sigmoid) function that can be used for soft thresholding in image processing. Unlike hard thresholding (which sets pixel values to either 0 or 255 based on a fixed cutoff), the logistic function allows a gradual transition between pixel intensities.

3. What is an image negative?

     A negative image is produced using the equation $S = L - 1 - r$, where $L$ is the total number of intensity levels, $r$ is the original pixel intensity, and $S$ is the new pixel value in the negative image. A negative image is simply the inversion of all intensity values.

4. What is the log transformation of an image?

    The log transformation of an image is used to enhance details in dark regions of an image by compressing high-intensity values and expanding low-intensity values.

5. Why is the power law (gamma correction) more versatile than log transformation?

    It is performed by using a lookup table

6. What is the utility of bit plane slicing in the piecewise-linear transformation?

    Image compression

7. What is the equation for histogram equalization?

    $h(v) = round(\frac{cdf(v) - cdf_{min}}{(M \times N) - cdf_{min}} \times (L - 1))$

8. What is histogram matching?

    Histogram Matching (also called Histogram Specification) is a digital image processing technique used to transform the histogram of one image to match the histogram of another image. Process:

    * Compute the histogram
    * Compute the CDF
    * Find the mapping function
    * Apply the transformation

## Lecture 5: [Filtering I](../_lectures_/05_Filtering-I.pdf)

1. Linear functions:

    * Correlation (computation):

    * Convolution (correlation, but filter is "flipped") (computation): 

2. Order statistics: e.g. average

3. Box filter:

    * Denoising: *Averages* noise out of image

    * Impulse filter: Size is 1x1.

    * Sharpen filter: Sharpens image.

4. Gaussian filter:

    * What is the effect of the Gaussian filter compared to a box filter?

        With a box filter, the resulting image will have sharp transitions between regions, with blocky artifacts near edges. With a Gaussian filter, the blur is more gradual, and edges are smoother with no harsh boundaries.

    * Explain the following properties of the Gaussian filter:

        * Recursive: 

            A recursive Gaussian filter refers to the ability of the filter to be applied in a recursive manner, which helps in computational efficiency.

            In the case of Gaussian filtering, the recursive property allows the filter to be implemented efficiently using two passes (one horizontal, one vertical) rather than applying a full 2D Gaussian kernel.

        * Product & convolution: 

            The product and convolution property refers to the relationship between multiplication and convolution. Convolution in the spatial domain is related to multiplying in the frequency domain.

        * Separability: 
        
            The Gaussian filter is a separable kernel. Blur with 1D Gaussian filter in one direction, then the other. The separability property of the Gaussian filter refers to the fact that the 2D Gaussian filter can be separated into two 1D filters, one applied in the horizontal direction and the other in the vertical direction.

## Lecture 6: [Filtering II](../_lectures_/06_Filtering-II.pdf)

1. The sum of coefficients in edge detection is: 0

2. Describe the Robert cross.

    The Roberts cross operator is a differential operator that approximates an image’s gradient via discrete differentiation, which is accomplished by computing the sum of the squares of the differences between diagonally adjacent pixels.

3. Explain the Sobel filter.

    It is used to highlight areas of an image where there is a rapid intensity change, which typically corresponds to edges or boundaries between different regions of the image.

4. Explain 2D isotropic filters.

    A 2D isotropic filter is a filter that has the same properties in all directions. The term isotropic refers to the fact that the filter behaves equally in all orientations (i.e., it doesn't prefer one direction over another).

5. Provide an example of a filtering operation for each application category:

    * Image segmentation: Adaptive threshold filtering

    * Object detection: Normalized cross-correlation

    * Image enhancement: Bilateral filtering

## Lecture 7: [Transformation I](../_lectures_/07_Transformation-I.pdf)

1. What is the formalization of an image translation?

    $\begin{align}
        \begin{bmatrix}
            x_1 \\
            y_1
        \end{bmatrix} \rightarrow 
        \begin{bmatrix}
            x_2 \\
            y_2
        \end{bmatrix} =
        \begin{bmatrix}
            x_1 + a \\
            y_1 + b
        \end{bmatrix} =
        \begin{bmatrix}
            1~0~a \\
            0~1~b
        \end{bmatrix}
        \begin{bmatrix}
            x_1 \\
            y_1 \\
            1
        \end{bmatrix}
    \end{align}$

2. What is the formalization of an image scaling?

    $\begin{align}
        \begin{bmatrix}
            x_1 \\
            y_1
        \end{bmatrix} \rightarrow 
        \begin{bmatrix}
            x_2 \\
            y_2
        \end{bmatrix} =
        \begin{bmatrix}
            ax_1 \\
            by_1
        \end{bmatrix} =
        \begin{bmatrix}
            a~0~0 \\
            0~b~0
        \end{bmatrix}
        \begin{bmatrix}
            x_1 \\
            y_1 \\
            1
        \end{bmatrix}
    \end{align}$

3. What is the formalization of an image rotation?

    $\begin{align}
        \begin{bmatrix}
            x_1 \\
            y_1
        \end{bmatrix} \rightarrow 
        \begin{bmatrix}
            x_2 \\
            y_2
        \end{bmatrix} =
        \begin{bmatrix}
            cos(\alpha)~sin(\alpha) \\
            -sin(\alpha)~cos(\alpha)
        \end{bmatrix}
        \begin{bmatrix}
            x_1 \\
            y_1
        \end{bmatrix} =
        \begin{bmatrix}
            cos(\alpha)~sin(\alpha)~0 \\
            -sin(\alpha)~cos(\alpha)~0
        \end{bmatrix}
        \begin{bmatrix}
            x_1 \\
            y_1 \\
            1
        \end{bmatrix}
    \end{align}$

4. What is the formalization of an affine transformation?

    $\begin{align}
        \begin{bmatrix}
            x_1 \\
            y_1
        \end{bmatrix} \rightarrow 
        \begin{bmatrix}
            x_2 \\
            y_2
        \end{bmatrix} =
        \begin{bmatrix}
            S_x~0 \\
            0~S_y
        \end{bmatrix}
        \begin{bmatrix}
            cos(\alpha)~sin(\alpha) \\
            -sin(\alpha)~cos(\alpha)
        \end{bmatrix}
        \begin{bmatrix}
            x_1 \\
            y_1
        \end{bmatrix} +
        \begin{bmatrix}
            t_x \\
            t_y
        \end{bmatrix} =
        \begin{bmatrix}
            ax_1 + by_1 + c \\
            dx_1 + ey_1 + f
        \end{bmatrix} =
        \begin{bmatrix}
            a~b~c \\
            d~e~f
        \end{bmatrix}
        \begin{bmatrix}
            x_1 \\
            y_1 \\
            1
        \end{bmatrix}
    \end{align}$

## Lecture 8: [Transformation II](../_lectures_/08_Transformation-II.pdf)

1. How do we deal with arbitrary trnasformations?

    Backwards mapping

2. What are the three steps of image registration?

    * Intensity-based registration (Direct): Aligns images by maximizing a similarity metric, such as mutual information or cross-correlation, between pixel intensities.

    * Feature-based registration: Identifies distinct features (e.g., key points, edges, corners) in images and finds correspondences between them.

    * Model-based (Transform-based): Relies on predefined transformation models (e.g., affine, projective, rigid, or non-rigid transformations) to align images.

3. What is blob detection?

    Blobs are homogenous regions that stand out from the background of an image. Detection highlights keypoints that are scale- and rotation-invariant.

4. How is the 2nd derivative of the Gaussian distribution related to the normalized Laplacian?

    The Laplacian of Gaussian (LoG) is obtained by taking the second derivative of the Gaussian function. The normalized Laplacian of Gaussian scales the LoG by σ2σ2 to ensure scale invariance. This is widely used in blob detection (e.g., in the scale-invariant Laplacian blob detector) and edge detection techniques.

5. How is the SIFT descriptor constructed?

    * Scale-space construction
    * Keypoint detection
    * Keypoint refinement
    * Orientation assignment
    * Descriptor construction
    * Descriptor normalization

6. What are the properties of the SIFT descriptor?

    * Scale-invariant: due to multi-scale detection
    * Rotation-invariant: due to dominant orientation assignment
    * Illumination-invariant: due to gradient-based representation and normalization
    * Highly distinctive: 128-dimensional vector captures local image patterns

7. How does one find the matches between paired points?

    * Brute-force: Computes the Euclidean distance or Hamming distance between all feature descriptors in two images. The nearest neighbor with the smallest distance is considered a match.

    * k-Nearest Neighbors (k-NN) Matching: Finds the k nearest neighbors for each descriptor.

    * FLANN (Fast Library for Approximate Nearest Neighbor): Uses optimized search structures like kd-trees or hierarchical k-means trees for faster matching

8. How does one deal with bad matches in the RANSAC algorithm?

    * Select a random subset: Randomly pick a small subset of matched points (e.g., 4 or more for homography).
    * Estimate a Transformation Model: Compute a transformation (e.g., homography, affine transformation, or fundamental matrix) using the selected points.
    * Find Inliers: Apply the estimated model to all matched points and count how many fit within a tolerance threshold (e.g., reprojection error < some epsilon)
    * Repeat the Process: Iterate multiple times (e.g., 1000 iterations) and choose the model with the most inliers.
    * Recompute the Model: Use the inliers to compute a refined model.

## Lecture 9: [Segmentation](../_lectures_/09_Image-Segmentation.pdf)

1. What are the 3 types of segmentation tasks?

    * Semantic: Classifies each pixel into a category (e.g., road, car, person, sky).

    * Instance: Like semantic segmentation, but distinguishes between different instances of the same object class.

    * Panoptic: A combination of semantic and instance segmentation. Assigns both a class label and an instance ID to each pixel.

2. In semantic segmentation, what are:

    * Thresholding?

        A fixed threshold TT is chosen, and pixels are classified as foreground or background.

    * Ostu thresholding?

        Finds an optimal threshold automatically by minimizing intra-class variance (i.e., within-class variance of foreground and background).

    * Adaptive thresholding?

        Uses different thresholds for different parts of an image, useful for varying lighting conditions. Computes the threshold based on the local neighborhood’s mean or Gaussian-weighted mean.

3. In Post-Processing, what are:

    * Common morphological operations?

        * Erosion: Shrinking objects in an image

        * Dilation: Expanding objects in an image

        * Opening: Remove small noise using erosion followed by dilation

        * Closing: Fills small holes using dilation followed by erosion

    * The two basic operations?

        * Erosion: Shrinking objects in an image

        * Dilation: Expanding objects in an image

    * Other opertaions?

        * Thinning/thickening: Thinning successively erodes object edges without breaking connectivity. Thickening is similar to dilation, but selectively adds pixels without merging objects.

        * Hole filling: Fills enclosed holes inside objects.