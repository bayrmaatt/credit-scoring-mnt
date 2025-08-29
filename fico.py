import streamlit as st
import pandas as pd

def score_payment_history(late_payments, total_months):
    if total_months == 0:
        return 50
    late_ratio = late_payments / total_months
    if late_ratio == 0:
        return 100
    elif late_ratio < 0.02:
        return 95
    elif late_ratio < 0.05:  
        return 85
    elif late_ratio < 0.10:  
        return 70
    elif late_ratio < 0.20:  
        return 50
    else:
        return 20

def score_amounts_owed(current_balance, credit_limit):
    if credit_limit == 0:
        return 50
    utilization = current_balance / credit_limit
    if utilization == 0:
        return 100
    elif utilization < 0.10:  
        return 95
    elif utilization < 0.30:  
        return 80
    elif utilization < 0.50:  
        return 60
    elif utilization < 0.70:  
        return 40
    elif utilization < 0.90:  
        return 25
    else:
        return 10

def score_credit_history(history_years):
    if history_years >= 10:
        return 100
    elif history_years >= 7:
        return 90
    elif history_years >= 5:
        return 80
    elif history_years >= 3:
        return 70
    elif history_years >= 2:
        return 60
    elif history_years >= 1:
        return 50
    else:
        return 30

def score_new_credit(inquiries_6months):
    if inquiries_6months == 0:
        return 100
    elif inquiries_6months == 1:
        return 90
    elif inquiries_6months == 2:
        return 75
    elif inquiries_6months == 3:
        return 60
    elif inquiries_6months == 4:
        return 45
    elif inquiries_6months == 5:
        return 35
    else:
        return 20

def score_credit_mix(credit_types):
    if credit_types >= 5:
        return 100
    elif credit_types == 4:
        return 90
    elif credit_types == 3:
        return 80
    elif credit_types == 2:
        return 65
    elif credit_types == 1:
        return 45
    else:
        return 20

def calculate_fico_score(payment_score, amounts_score, history_score, new_credit_score, mix_score):
    weighted_score = (
        payment_score * 0.35 +      
        amounts_score * 0.30 +      
        history_score * 0.15 +      
        new_credit_score * 0.10 +   
        mix_score * 0.10            
    )
    
    fico_score = 300 + (weighted_score / 100) * 550
    return round(fico_score)

def get_score_category(score):
    if score >= 700:
        return "Онцгой сайн", "#4CAF50"
    elif score >= 630:
        return "Маш сайн", "#8BC34A"
    elif score >= 600:
        return "Сайн", "#FFC107"
    elif score >= 580:
        return "Боломжийн", "#FF9800"
    else:
        return "Маш муу", "#F44336"

def format_money(amount):
    return f"{amount:,.0f}₮"

st.set_page_config(
    page_title="FICO Score Calculator",
    layout="wide"
)

st.title(" FICO Оноо Тооцоолуур")
st.markdown("---")

st.markdown("""
### FICO онооны 5 үндсэн шалгуур үзүүлэлт:
- **Эргэн төлөлт** (35%): Хугацаандаа төлөлтөө хийсэн түүх
- **Зээлийн үлдэгдэл** (30%): Одоогийн зээлийн үлдэгдэл  
- **Зээлийн түүх** (15%): Зээлийн данс ашигласан хугацаа
- **Шинэ зээл лавлагаа** (10%): Авсан зээлийн лавлагааны тоо
- **Зээлийн багц** (10%): Авсан зээлийн төрлүүд
""")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader(" Харилцагчийн мэдээлэл")
    
    customer_name = st.text_input("Харилцагчийн нэр:", placeholder="Жишээ: Баярмаа")
    
    st.markdown("#### Зээлийн мэдээлэл")
    
    st.markdown("**Эргэн төлөлтийн түүх**")
    col1_1, col1_2 = st.columns(2)
    with col1_1:
        late_payments = st.number_input(
            "Хугацаа хэтэрсэн төлөлтийн тоо:",
            min_value=0, value=2, step=1,
            help="Сүүлийн 24 сарын хувьд хугацаа хэтрүүлж төлсөн төлбөрийн тоо"
        )
    with col1_2:
        total_months = st.number_input(
            "Нийт сар:",
            min_value=1, value=24, step=1,
            help="Зээлийн нийт сар"
        )
    
    st.markdown("**Зээлийн үлдэгдэл**")
    col2_1, col2_2 = st.columns(2)
    with col2_1:
        current_balance = st.number_input(
            "Одоогийн зээлийн үлдэгдэл (₮):",
            min_value=0, value=3000000, step=100000,
            help="Одоогийн нийт зээлийн үлдэгдэл"
        )
    with col2_2:
        credit_limit = st.number_input(
            "Нийт зээлийн лимит (₮):",
            min_value=1, value=10000000, step=100000,
            help="Бүх зээлийн нийт лимит"
        )
    
    st.markdown("**Зээлийн түүх**")
    history_years = st.number_input(
        "Зээлийн түүхийн жил:",
        min_value=0.0, max_value=50.0, value=5.5, step=0.5,
        help="Анхны зээл авснаас хойших жил"
    )
    
    st.markdown("**Шинэ зээл лавлагаа**")
    inquiries_6months = st.number_input(
        "Сүүлийн 6 сарын лавлагаа:",
        min_value=0, value=1, step=1,
        help="Сүүлийн 6 сарын зээлийн лавлагаа/хүсэлт авсан тоо"
    )
    
    st.markdown("**Зээлийн багц**")
    credit_types = st.selectbox(
        "Зээлийн төрлийн тоо:",
        options=[0, 1, 2, 3, 4, 5, 6],
        index=3,
        help="Ямар төрлийн зээл байгаа вэ? (кредит карт, автомашины зээл, ипотекийн зээл г.м.)"
    )
    
    st.markdown("*Зээлийн төрлүүд: Кредит карт, Автомашины зээл, Ипотекийн зээл, Оюутны зээл, Бизнесийн зээл*")

with col2:
    st.subheader(" Үр дүн")
    
    payment_score = score_payment_history(late_payments, total_months)
    amounts_score = score_amounts_owed(current_balance, credit_limit)
    history_score = score_credit_history(history_years)
    new_credit_score = score_new_credit(inquiries_6months)
    mix_score = score_credit_mix(credit_types)
    
    fico_score = calculate_fico_score(
        payment_score, amounts_score, history_score, new_credit_score, mix_score
    )
    
    category, color = get_score_category(fico_score)
    
    if customer_name:
        st.success(f"**{customer_name}**-ын FICO оноо:")
    
    st.markdown(f"""
    <div style='text-align: center; padding: 30px; border: 3px solid {color}; border-radius: 15px; background-color: #f8f9fa; margin: 20px 0;'>
        <h1 style='color: {color}; margin: 0; font-size: 4em; font-weight: bold;'>{fico_score}</h1>
        <h2 style='color: {color}; margin: 10px 0; font-size: 1.5em;'>{category}</h2>
        <p style='margin: 0; color: #666; font-size: 1.1em;'>300-850 онооны хооронд</p>
    </div>
    """, unsafe_allow_html=True)
    
    progress = (fico_score - 300) / 550
    st.progress(progress)
    st.write(f"Прогресс: {progress:.1%}")
    
    if credit_limit > 0:
        utilization = (current_balance / credit_limit) * 100
        st.info(f"Зээл ашиглалт: {utilization:.1f}%")

st.markdown("---")
st.subheader(" Дэлгэрэнгүй задаргаа")

components_data = {
    "Шалгуур үзүүлэлт": [
        "Эргэн төлөлт", 
        "Зээлийн үлдэгдэл", 
        "Зээлийн түүх", 
        "Шинэ зээл лавлагаа", 
        "Зээлийн багц"
    ],
    "Жин (%)": ["35%", "30%", "15%", "10%", "10%"],
    "Бодит утга": [
        f"{late_payments}/{total_months} хугацаа хэтрэлттэй",
        f"{format_money(current_balance)} / {format_money(credit_limit)}",
        f"{history_years} жил",
        f"{inquiries_6months} удаа лавлагаа авсан",
        f"{credit_types} төрлийн зээл"
    ],
    "Оноо": [payment_score, amounts_score, history_score, new_credit_score, mix_score],
    "Хувь нэмэр": [
        f"{payment_score * 0.35:.1f}",
        f"{amounts_score * 0.30:.1f}",
        f"{history_score * 0.15:.1f}",
        f"{new_credit_score * 0.10:.1f}",
        f"{mix_score * 0.10:.1f}"
    ]
}

df = pd.DataFrame(components_data)
st.dataframe(df, use_container_width=True, hide_index=True)

st.markdown("---")
st.subheader(" FICO оноогийн ангилал")

col3, col4, col5, col6, col7 = st.columns(5)

score_ranges = [
    ("390-579", "Маш муу", "#F44336"),
    ("580-599", "Боломжийн", "#FF9800"),
    ("600-629", "Сайн", "#FFC107"),
    ("630-699", "Маш сайн", "#8BC34A"),
    ("700+", "Онцгой сайн", "#4CAF50")
]

cols = [col3, col4, col5, col6, col7]

for i, (score_range, label, color) in enumerate(score_ranges):
    with cols[i]:
        is_current = False
        if i == 0 and fico_score < 580:
            is_current = True
        elif i == 1 and 580 <= fico_score < 600:
            is_current = True
        elif i == 2 and 600 <= fico_score < 630:
            is_current = True
        elif i == 3 and 630 <= fico_score < 700:
            is_current = True
        elif i == 4 and fico_score >= 700:
            is_current = True
        
        indicator = " Та энд байна" if is_current else ""
        
        st.markdown(f"""
        <div style='text-align: center; padding: 15px; border: 2px solid {color}; border-radius: 10px; 
                    background-color: {"#e8f5e8" if is_current else "#f9f9f9"}; margin: 5px 0;'>
            <h4 style='color: {color}; margin: 5px 0;'>{score_range}</h4>
            <p style='margin: 5px 0; font-weight: bold;'>{label}</p>
            <p style='margin: 0; color: red; font-size: 0.9em;'>{indicator}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.subheader(" Зөвлөмж")

recommendations = []

if payment_score < 70:
    recommendations.append(f" **Эргэн төлөлт сайжруулах**: Сарын {late_payments}/{total_months} хугацаа хэтрэлттэй байна. Төлбөрөө цаг тухайд нь хийж, хугацаа хэтрүүлэлтийг багасгах.")

if amounts_score < 60:
    utilization_percent = (current_balance / credit_limit) * 100
    recommendations.append(f" **Зээлийн үлдэгдэл багасгах**: {utilization_percent:.1f}% ашиглаж байна. 30%-аас доош болгох.")

if history_score < 60:
    recommendations.append(f" **Зээлийн түүх уртасгах**: {history_years} жилийн зээлийн түүхтэй.")

if new_credit_score < 70:
    recommendations.append(f" **Шинэ зээлийн лавлагаа хязгаарлах**: 6 сард {inquiries_6months} лавлагаа авсан. 2-3 илүү лавлагаа авахгүй байх.")

if mix_score < 60:
    recommendations.append(f" **Зээлийн багц**: {credit_types} төрөлтэй. ")

if recommendations:
    for rec in recommendations:
        st.info(rec)
else:
    st.success(" Зээлийн түүх сайн байна! Одоогийн байдлаа хадгалахыг хичээгээрэй.")

st.markdown("---")
st.subheader(" Зээлийн ашиглалтын шалгуур")

col_guide1, col_guide2 = st.columns(2)

with col_guide1:
    st.markdown("""
    **Зээлийн ашиглалтын хувь:**
    - 0-10%: Онцгой сайн 
    - 10-30%: Маш сайн 
    - 30-50%: Сайн 
    - 50-70%: Боломжийн 
    - 70%+: Маш муу 
    """)

with col_guide2:
    st.markdown("""
    **Хугацаа хэтрэлтийн хувь:**
    - 0%: Онцгой сайн 
    - 0-2%: Маш сайн 
    - 2-5%: Сайн 
    - 5-10%: Боломжийн 
    - 10%+: Маш муу 
    """)

st.markdown("---")
st.markdown("*Энэхүү FICO тооцоолох систем нь хувийн төсөл болно. Т.Баярмаа*")