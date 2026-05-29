from ultralytics import YOLO

model = YOLO("yolov8m.pt")

def detect_objects(image_path):

    results = model(image_path)

    detected = []

    for result in results:

        width = result.orig_shape[1]

        for box in result.boxes:

          confidence = float(box.conf[0])

          if confidence < 0.5:
            continue

          cls_id = int(box.cls[0])
          label = model.names[cls_id]

          x1, y1, x2, y2 = box.xyxy[0]

          center_x = (x1 + x2) / 2

          if center_x < width / 3:
                position = "left"

          elif center_x < (2 * width / 3):
                position = "center"

          else:
                position = "right"

          detected.append({
                "label": label,
                "position": position,
                "confidence": round(confidence, 2)
            })

    return detected

def summarize_objects(detected_objects):

    summary = {}

    for obj in detected_objects:

        label = obj["label"]
        position = obj["position"]

        if label not in summary:
            summary[label] = set()

        summary[label].add(position)

    messages = []

    for label, positions in summary.items():

        if len(positions) >= 3:
            if label == "person":
                messages.append("People detected around you")
            elif label == "car":
                messages.append("Cars detected around you")
            else:
                messages.append(f"{label.capitalize()}s detected around you")

        else:
            pos_text = ", ".join(sorted(positions))

            if label == "person":
                messages.append(f"Person detected on {pos_text}")
            else:
                messages.append(
                    f"{label.capitalize()} detected on {pos_text}"
                )

    return messages

def create_speech_summary(summary):
    return ". ".join(summary) + "."