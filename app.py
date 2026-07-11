# SteelVision AI MVP - app.py
import streamlit as st
from PIL import Image
import pandas as pd
from utils.model import detect_objects
from utils.inspection import calculate_health, machine_status, maintenance_priority, recommendation

st.set_page_config(page_title="SteelVision AI", page_icon="🏭", layout="wide")

st.markdown("""
<style>
body {font-family:Segoe UI;}
.metric {padding:10px;border-radius:10px;background:#1f2937;}
</style>
""", unsafe_allow_html=True)

def map_to_defects(detections):
    mapping={
        "person":"Loose Bolt",
        "car":"Surface Damage",
        "truck":"Rust",
        "bus":"Corrosion",
        "motorcycle":"Damaged Belt",
        "bicycle":"Loose Bolt",
    }
    return [mapping[d["class"]] for d in detections if d["class"] in mapping]

with st.sidebar:
    st.title("🏭 SteelVision AI")
    st.success("Hackathon MVP")
    st.write("Edge AI Industrial Inspection")
    st.divider()
    st.write("Upload an image or use webcam.")

st.title("🏭 SteelVision AI")
tab1,tab2=st.tabs(["Upload Image","Webcam"])

image=None
with tab1:
    up=st.file_uploader("Upload machine image",type=["jpg","jpeg","png"])
    if up:
        image=Image.open(up)

with tab2:
    cam=st.camera_input("Capture image")
    if cam:
        image=Image.open(cam)

if image is None:
    st.info("Upload or capture an image.")
    st.stop()

c1,c2=st.columns([2,1])
with c1:
    st.image(image,width="stretch")

progress=st.progress(0)
progress.progress(20)
annotated,detections=detect_objects(image)
progress.progress(70)

demo=map_to_defects(detections)
engine=[d.lower().replace(" ","_") for d in demo]
health=calculate_health(engine)
status=machine_status(health)
priority=maintenance_priority(health)
advice=recommendation(engine)
progress.progress(100)
progress.empty()

with c1:
    st.subheader("AI Detection")
    st.image(annotated,width="stretch")

with c2:
    st.metric("Health",f"{health}/100")
    st.metric("Status",status)
    st.metric("Priority",priority)
    st.metric("Defects",len(demo))

st.subheader("Detections")
df=pd.DataFrame(detections if detections else [{"class":"None","confidence":0}])
st.dataframe(df,width="stretch",hide_index=True)

if detections:
    csv=df.to_csv(index=False).encode()
    st.download_button("Download CSV",csv,"inspection.csv","text/csv")

st.subheader("Industrial Defects")
if demo:
    for d in demo:
        st.warning(d)
else:
    st.success("No visible defects detected.")

st.subheader("Maintenance Recommendation")
st.info(advice)

if health>=90:
    st.success("✅ Inspection Completed Successfully")
elif health>=60:
    st.warning("Inspection completed. Maintenance recommended.")
else:
    st.error("Critical machine condition detected!")

st.caption("SteelVision AI • Python • Streamlit • YOLO")
