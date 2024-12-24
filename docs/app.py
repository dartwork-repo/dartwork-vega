from pathlib import Path
import altair as alt
import streamlit as st
import vl_convert as vlc
from vega_datasets import data


class Section:
    def __init__(self):
        self.section = 0

    def __call__(self):
        self.section += 1
        return self.section

section = Section()


st.markdown("# Dartwork-Vega Project")
st.markdown(f"""
## {section()}. Introduction
이 문서는 dartwork-vega 프로젝트를 소개하는 문서입니다.
dartwork-vega 프로젝트는 dartwork에서 진행하는 데이터 시각화 프로젝트입니다.
이 프로젝트는 크게 2가지의 목적을 가집니다.
1. dartwork의 시각화 기반을 기존 Matplotlib에서 Vega, Vega-Lite, Vega-Altair로 전환합니다. 이는 Matplotlib의 한계를 극복하고 더 나은 시각화를 위해 노력하는 것을 목표로 합니다.
2. dartwork의 시각화 결과들을 모으는 공간을 만듭니다. 이는 분산된 시각화 결과물을 한 곳에 모아 관리하고 공유하는 것을 목표로 합니다.
""")

with st.expander("Vega 시리즈에 대한 소개"):
    st.markdown("""
                Vega, Vega-Lite, Vega-Altair의 관계는 다음과 같습니다:

* Vega는 D3를 기반으로 한 선언적 시각화 문법 시스템입니다. JSON 형식으로 차트를 정의하며, D3보다 높은 수준의 추상화를 제공합니다.

* Vega-Lite는 Vega의 상위 레벨 문법입니다. Vega보다 간단한 JSON 스펙으로 시각화를 생성할 수 있으며, 내부적으로 Vega 스펙으로 컴파일됩니다.

* Altair는 Python에서 Vega-Lite를 사용할 수 있게 해주는 라이브러리입니다. Python 객체와 메서드를 통해 Vega-Lite 스펙을 생성합니다.

계층 구조로 보면:
1. D3.js (최하위 레벨, 가장 유연하지만 복잡)
2. Vega (D3 기반, 선언적 방식)
3. Vega-Lite (Vega 기반, 더 간단한 문법)
4. Altair (Vega-Lite의 Python 인터페이스)

위로 갈수록 더 추상화되어 사용이 쉽지만, 커스터마이징 자유도는 낮아집니다.
""")


section_value = section()
st.markdown(f"""
## {section_value}. Vega를 사용해야 하는 이유
이 섹션에서는 Matplotlib대신 Vega 시리즈를 사용해야 하는 논리적 이유에 대해 설명합니다. 
Matplotlib은 Python의 시각화 라이브러리 중 가장 널리 사용되는 라이브러리 중 하나이지만,
Vega 시리즈를 사용하는 것이 더 나은 선택일 수 있습니다. 

이 문서는 Vega 시리즈를 사용해야 하는 이유를 다음과 같이 설명합니다:
1. **멀티플랫폼 지원**: Vega 시리즈는 JSON 형식으로 시각화를 정의하기 때문에 다양한 환경에서 동일한 시각화를 사용할 수 있습니다.
2. **상호작용 디자인 가능**: Vega 시리즈는 상호작용을 활용한 디자인이 가능합니다.
3. **재사용성**: Vega 시리즈는 JSON으로 시각화를 정의하기 때문에 재사용성이 높습니다.
4. **선택적 자유도**: Vega 시리즈는 다양한 추상화 수준을 제공합니다.
5. **상호작용성**: Vega 시리즈는 상호작용성을 위한 다양한 기능을 제공합니다.
""")


subsection = Section()
st.markdown(f"""### {section_value}.{subsection()}. 멀티플랫폼 지원""")
st.markdown("""
Matplotlib은 목적과 환경에 따라서 같은 시각화를 여러번 구현해야 한다는 문제가 있습니다. 논문과 발표자료
사이의 전환은 그나마 쉽게 가능하지만 웹과 데스크탑, 모바일 환경에서 동일한 시각화를 구현하는 것은 어렵습니다.
특히 웹에서 Matplotlib으로 렌더링 된 이미지를 사용하는 것은 굉장히 어색하여 세련되지 못한 느낌을 줍니다.
            
Vega 시리즈로 논문 피규어를 생성했다면 해당 결과물을 프레젠테이션부터 Dartwork 블로그, 웹사이트 등에
재사용하기가 훨씬 쉽습니다. 또한 Vega 시리즈는 JSON 형식으로 시각화를 정의하기 때문에 다양한 환경에서
동일한 시각화를 사용할 수 있습니다. 예를 들어, Vega-Lite로 작성된 JSON 파일을 불러와서 Altair로 렌더링하는 것이
가능합니다. 반대로 Altair로 작성된 JSON 파일을 불러와서 Vega-Lite로 웹 환경에서 렌더링하는 것도 가능합니다.
            
또한 JSON으로 구성된 선언적 특성 때문에 많은 챗봇 시스템과 시각화 도구에서 Vega-Lite가 활발하게 
활용되고 있습니다. Code를 생성하는 것이 아닌 JSON을 생성하는 것이 더 쉽기 때문입니다. Figma
같은 디자인 툴에서도 Vega-Lite를 활용하여 시각화를 디자인할 수 있습니다.
""")

st.image(
    Path(__file__).parent / "assets/graphpad.png",
    caption="Figma의 GraphPad 플러그인",
)

st.markdown(f"""### {section_value}.{subsection()}. 상호작용 디자인 가능""")
st.markdown("""
Matplotlib은 상호작용을 활용한 디자인이 굉장히 제한적입니다. 이는 Matplotlib이 정적 이미지를 생성하는
방식으로 동작하기 때문입니다. 이러한 제한으로 인해 사용자가 시각화 결과에 대해 상호작용을 할 수 있는 기능을
구현하기 어렵습니다. 만약 아래와 같은 Sankey diagram을 Matplotlib으로 최적화 한다고 하면 훨씬 더
많은 노력이 필요할 것입니다. 
""")

with open(Path(__file__).parent / "assets/sankey.html") as f:
    st.components.v1.html(scrolling=True, width=1000, height=830, html=f.read())

st.markdown(f"""### {section_value}.{subsection()}. 재사용성""")
st.markdown("""
Matplotlib의 상당한 자유도를 가지는 Python으로 작성되기 때문에 처음부터 범용성을 고려하고
작성된 시각화 코드가 아니라면 다른 시각화에 재사용하는 것이 까다롭습니다. 반면 Vega 시리즈는
논리적으로 구조화된 시각화 도구로 모든 시각화가 하나의 JSON 형식으로 표현되기 때문에 재사용성이
높습니다. 또한 논리적으로 설계된 틀 안에서 코드를 작성하기 때문에 더 간결한 코드를 작성할 수 있습니다.
제 경험만으로 판단할 때 Vega 시리즈로 작성하는 것이 Matplotlib으로 작성하는 것보다 더 빠르고
간결하게 작성할 수 있습니다.
""")

st.markdown("**Vega-Lite Example**")
with open(Path(__file__).parent / "assets/ridge.json") as f:
    json = f.read()

tab1, tab2 = st.columns(2)

with tab1:
    st.markdown("""Vega-Lite JSON""")
    st.json(json, expanded=False)
    # st.code(json)

with tab2:
    st.markdown("""Vega-Lite Chart""")
    chart = alt.Chart.from_json(json)
    st.altair_chart(chart)

st.markdown("""
또한 JSON으로 변환 가능하다는 것은 언제든 직렬화가 가능하다는 뜻이고 이는 상호작용을 통한 디자인에서
강점을 발휘합니다. 특정 시각화 파라미터 값의 상태값을 저장하고 불러오는 것이 쉽게 가능하기 때문입니다.
만약 Matplotlib으로 작성된 코드를 다른 환경에서 사용하려면 코드를 복사하고 붙여넣기 하는 것이 유일한 방법입니다.
혹은 직접 시각화 파라미터를 dictionary 형태로 설계한 뒤 저장하고 불러오는 방법을 사용해야 합니다.
""")

st.markdown(f"""### {section_value}.{subsection()}. 선택적 자유도""")
st.markdown("""Vega 시리즈는 Vega-Altair부터 D3.js까지 다양한 추상화 수준을 제공합니다. 
이는 사용자가 자신의 목적에 맞게 선택적으로 사용할 수 있다는 장점을 가집니다.""")

st.write("""**같은 기능을 하는 Vega-Lite JSON과 Vega JSON**: 저수준 Vega JSON은 더 많은 커스터마이징이 가능하지만,
         더 많은 코드를 작성해야 합니다. 반면 Vega-Lite JSON은 더 높은 수준의 추상화를 제공하며, 더 적은 코드로
         동일한 결과를 얻을 수 있습니다.""")

tab1, tab2 = st.columns(2)

with tab1:
    st.markdown("""Vega-Lite JSON""")
    exp1 = st.radio("Expand", [True, False], horizontal=True, index=1)
    st.json(json, expanded=bool(exp1))
    # st.code(json)

with tab2:
    st.markdown("""Vega JSON""")
    chart = alt.Chart.from_json(json)
    exp2 = st.radio("Expand", [True, False], horizontal=True, index=1, key='exp2')
    st.json(chart.to_json(format="vega"), expanded=exp2)


st.markdown(f"""### {section_value}.{subsection()}. 상호작용성""")
st.markdown("""
Vega 시리즈는 상호작용성을 위한 다양한 기능을 제공합니다. 이는 사용자가 시각화 결과에 대해 상호작용을 할 수 있게
해주는 기능으로, 사용자가 시각화 결과에 대해 더 깊이 있는 분석을 할 수 있게 도와줍니다.
""")

st.markdown("**Vega-Lite Interaction Example**")
source = data.seattle_weather()

color = alt.Color('weather:N').scale(
    domain=['sun', 'fog', 'drizzle', 'rain', 'snow'],
    range=['#e7ba52', '#a7a7a7', '#aec7e8', '#1f77b4', '#9467bd']
)

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=['x'])
click = alt.selection_point(encodings=['color'])

# Top panel is scatter plot of temperature vs time
points = alt.Chart().mark_point().encode(
    alt.X('monthdate(date):T').title('Date'),
    alt.Y('temp_max:Q')
        .title('Maximum Daily Temperature (C)')
        .scale(domain=[-5, 40]),
    alt.Size('precipitation:Q').scale(range=[5, 200]),
    color=alt.when(brush).then(color).otherwise(alt.value("lightgray")),
).properties(
    width=550,
    height=300
).add_params(
    brush
).transform_filter(
    click
)

# Bottom panel is a bar chart of weather type
bars = alt.Chart().mark_bar().encode(
    x='count()',
    y='weather:N',
    color=alt.when(click).then(color).otherwise(alt.value("lightgray")),
).transform_filter(
    brush
).properties(
    width=550,
).add_params(
    click
)

chart = alt.vconcat(
    points,
    bars,
    data=source,
    title="Seattle Weather: 2012-2015"
)

st.altair_chart(chart)

# # Save as json
# with open(Path(__file__).parent / "assets/interactive.json", "w") as f:
#     f.write(chart.to_json())