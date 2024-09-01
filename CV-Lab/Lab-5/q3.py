import cv2
import numpy as np
import matplotlib.pyplot as plt

def compute_dp(img, nsc, k=1.2):
    py = [img]
    sigma = 1.0  # Initial sigma
    for _ in range(nsc - 1):
        sigma *= k
        img_blurred = cv2.GaussianBlur(img, (0, 0), sigma)
        py.append(img_blurred)

    dp = [py[i+1] - py[i] for i in range(len(py) - 1)]
    return dp

def detect_kp(dp, thrs=0.03):
    kp = []
    for i, dog in enumerate(dp):
        mask = np.abs(dog) > thrs * np.max(np.abs(dog))
        kp.extend([(i, x, y) for x, y in zip(*np.nonzero(mask))])
    return kp

def extract(img, kp, ps=16):
    descs = []
    half = ps // 2

    for si, x, y in kp:
        sc = 1.2 ** si
        patch = img[max(0, int(x - half)):int(x + half),
                      max(0, int(y - half)):int(y + half)]

        if patch.shape[0] < ps or patch.shape[1] < ps:
            continue

        patch = cv2.resize(patch, (ps, ps))
        patch = patch.astype(np.float32)
        desc = patch.flatten()
        desc /= np.linalg.norm(desc)
        descs.append(desc)

    return np.array(descs)

def draw_keypoints(img, kp):
    img_kp = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    for si, x, y in kp:
        cv2.circle(img_kp, (int(y), int(x)), 4, (0, 255, 0), -1)
        cv2.putText(img_kp, f'{si}', (int(y), int(x) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
    return img_kp

def main():
    img_path = 'Untitled.jpeg'
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    dp = compute_dp(img, nsc=3)
    kp = detect_kp(dp)

    dc = extract(img, kp)

    img_kp = draw_keypoints(img, kp)

    plt.imshow(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB))
    plt.title('Keypoints detected manually')
    plt.axis('off')
    plt.show()

    print(f"Custom Descriptors: {dc.shape}")

if __name__ == "__main__":
    main()
