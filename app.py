import streamlit as st
from PIL import Image
import base64
from io import BytesIO


st.set_page_config(page_title="فوتو - ساحل طلایی",page_icon="logo.png")


with open('c.css') as f:
    st.markdown(f"<style> {f.read()} </style>",unsafe_allow_html=True)


def main():
    cv1, cv2 = st.columns([3,3])

    with cv1:
        with st.expander(expanded=True,label="هتل ساحل طلایی قشم"):
            
            st.video("vidd.mp4",)
            
            c1,c2,c3 = st.columns(3)
            with c1:
     # st.markdown(f'<a href="tel:{phone_number}">{phone_number}</a>', unsafe_allow_html=True)
                st.markdown("[شمار ه تماس](tel:989025342900)")
    
    
            with c2:

                st.image('logo.png',width=60)

            with c3:
                st.markdown("[وبسایت](https://goldenbeachhotel.ir)")


    
            st.divider()
            st.markdown("""
هتل ساحل طلایی در 11 کیلومتری قشم است. این هتل قبل‌ها به ساحل سیمین یا پلاژ سیمین معروف بوده. هتل ساحل طلایی از همه نظر هتلی بی‌نظیر در قشم است و طیف گسترده‌ای از خدمات و امکانات را در اختیار مسافران قرار می‌دهد. ساحل اختصاصی هتل بسیار تمیز و خلوت است علاوه بر این‌ها مسافران می‌توانند لذت ماهیگیری را در اسکله‌ی تفریحی هتل تجربه کنند. هتل ساحل طلایی چند نوع واحد اقامتی دارد: سوئیت و اتاق معمولی،سوئیتهای وی آی پی، دوبلکس دوطبقه هم دارند. رستوران ساحلی دوطبقه با نمای رو به دریا و آلاچیق‌های چوبی کنار ساحل همواره برای مسافران خاطرات خوشی رقم زده. هتل ساحل طلایی در جاده‌ی ساحلی جنوبی و در کنار زیارتگاه شاه شهید واقع شده. این هتل کمتر از ۲۰ دقیقه با یکی از جاذبه‌های شگفت‌انگیز قشم فاصله دارد. دره‌ی ستاره‌ها با قدمتی دو میلیون ساله، یکی از جاذبه‌های طبیعی قشم است که صحبت از آن همیشه با داستان‌ها و گاهی خرافه‌های جالبی همراه بوده. اقامت در هتل ساحل طلایی و بازدید از این نقاط دیدنی می‌تواند بدل به یکی از بهترین تجربیات مسافران قشم شود.


""")

        
    with cv2:
        st.title("فوتو - ساحل طلایی")
        st.divider()

        st.write("""
        # فوتو
تغییر اندازه عکس خیلی سریع کافیه پایین ⬇️ صفحه برید و عکس دلخواه خود را آپلود کنید و اندازه خود را تغییر دهید و در آخر گزینه دانلود رو بزنید
""")

    st.divider()

    # بارگذاری تصویر
    uploaded_image = st.file_uploader("تصویر را انتخاب کنید", type=["jpg", "jpeg", "png",])

    if uploaded_image is not None:
        # باز کردن تصویر با استفاده از PIL
        image = Image.open(uploaded_image)

        # نمایش تصویر قبل از بزرگنمایی
        st.subheader("تصویر قبل از بزرگنمایی")
        st.image(image, use_column_width=True)

        # بزرگنمایی تصویر
        width = st.slider("عرض تصویر (پیکسل)", 100, 2000, 500)
        height = st.slider("ارتفاع تصویر (پیکسل)", 100, 2000, 500)
        resized_image = image.resize((width, height))

        # نمایش تصویر بعد از بزرگنمایی
        st.subheader("تصویر بعد از بزرگنمایی")
        st.image(resized_image, use_column_width=True)

        # دکمه دانلود تصویر بزرگنمایی شده
        download_button(resized_image)

def download_button(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{img_str}" download="resized_image.png">دانلود تصویر ویرایش شده</a>'
    st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

st.divider()

st.markdown("[ساخته شده توسط عبدالله چلاسی](https://abdollahchelasi.streamlit.app/)")
