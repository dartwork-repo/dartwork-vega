# Vega 개발 환경

필요 사전 지식
1. HTML 기본 구성 `<head>`, `<body>`, `<script>`
2. CDN
3. JSON
4. JavaScrip의 fetch 함수
5. [vega-embed](https://github.com/vega/vega-embed)
6. [Vega View API](https://vega.github.io/vega/docs/api/view/)

## 1. 구성 요소

한 그래프는 하나의 폴더로 관리되며 해당 폴더에는 다음과 같은 파일이 존재한다.

* `data`: 시각화에 필요한 데이터가 저장된 폴더
* `vega`: `vega`, `vega-lite`, `vega-embed`의 기능이 구현된 JavaScript파일이 저장된 폴더. 인터넷이 연결된 경우 필요없음. 일반적으로 이 폴더를 수정할 일은 없습니다.
* `index.vl.json`: Vega-Lite Spec이 작성된 JSON 파일
* `index.html`: 시각화에 필요한 HTML, Vega spec, JavaScript가 작성된 파일


## 2. 구성 설명

### 2-1. `data`
시각화에 필요한 데이터를 저장합니다. Vega가 지원하는 어떤 형식도 가능합니다. 일반적으로 `index.vl.json`에서 `url`로 사용됩니다.

### 2-2. `index.vl.json`
시각화에 필요한 Vega-Lite 스펙을 작성한 JSON파일입니다. VSCode 에서 JSON에 `$schema`가 등록되어 있으면 인텔리센스나 벨리데이션이 작동하여 좀 더 쉽게 Vega-Lite Spec을 작성할 수 있습니다. 아래는 자동완성의 예시입니다.


![자동 완성 예시](assets/intellisense.png)

Vega-Lite 스펙을 HTML안에 작성할 수도 있으나 인텔리센스나 벨리데이션을 활용하기 위하여 JSON으로 분리하였습니다.

또한 2-1에서 설명한 것과 같이 위 JSON파일에서 데이터를 로드합니다.
```json
    "data": {
      "url": "data/my_data.csv"
    },
```
### 2-3. `index.html`
실제로 시각화 작동에 필요한 HTML 파일입니다.

`<head>` 테그에서 실제 Vega 렌더링에 필요한 기능을 로딩합니다. 인터넷이 연결된 경우 CDN 주소에서 로딩해도 되지만 인터넷이 없는 환경을 고려하여 `vega`폴더에 같은 파일을 미리 다운로드하였습니다.
```html
  <head>
    <title>Embedding Vega-Lite</title>
    <!-- 인터넷이 연결된 경우 아래 주석 처리된 CDN 주소를 사용하면 됩니다. -->
    <!-- <script src="https://cdn.jsdelivr.net/npm/vega@5.30.0"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-lite@5.21.0"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-embed@6.26.0"></script> -->

    <!-- 인터넷이 연결되지 않은 경우 로컬에 다운로드한 파일을 사용하면 됩니다. -->
    <script src="vega/vega@5.30.0.js"></script>
    <script src="vega/vega-lite@5.21.0.js"></script>
    <script src="vega/vega-embed@6.26.0.js"></script>

  </head>
```

다음은 vega 시각화가 렌더링 될 html 요소를 정의합니다. 나중에 vega 시각화 결과가 `vis`라는 id를 가지는 `<div>`요소의 자식 요소로 렌더링 됩니다.
```html
<div id="vis"></div>
```

다음은 필요한 JavaScript를 작성합니다. 아래 예시는 최소한의 예시를 작성했습니다 (주석 참고).
```html
    <script>
        // JSON 파일을 로딩합니다.
        fetch('index.vl.json')
            // 로딩이 성공하면 결과를 JSON으로 변환합니다.
            .then(response => response.json())
            // JSON 변환이 성공하면 Vega Embed를 사용하여 시각화를 생성합니다.
            .then(spec => {
                // #vid 요소에 spec을 이용하여 시각화를 생성합니다.
                vegaEmbed('#vis', spec)
                    // 시각화 생성이 성공하면 vega-view 오브젝트 등으로
                    // 원하는 기능을 구현합니다. 일반적으로 따로 구현하는 경우는 드뭅니다.
                    // 웹 브라우저에서 개발자 도구를 이용하여 vega-view 오브젝트를 확인하면 됩니다.
                    .then(result => {
                        let view = result.view;
                        console.log('Vega Embed Result:', result);
                        console.log('Vega View:', view);
                        // Visualization was successfully created
                    })
                    // 시각화 생성이 실패하면 에러를 출력합니다.
                    .catch(error => {
                        console.error('Vega Embed Error:', error);
                    });
            })
            // JSON 변환이 실패하면 에러를 출력합니다.
            .catch(error => {
                console.error('Error loading JSON:', error);
            });
    </script>
```

Vega-Spec을 렌더링하기 위하여 라이브러리에서 지원하는 `vegaEmbed`를 사용합니다.


HTML속 JavaScript를 활용하는 두가지 이유가 있습니다.
1. `node.js`의 설치가 필요 없음
2. Vega-Spec을 통하여 랜더링 한 결과와 상호작용할 수 있음 (View API와 JavaScript 코드 활용해야 함)

2의 경우 직접 HTML Element나 Event를 직접 처리해서 더 강력한 상호작용을 구현할 수 있습니다 (`D3.js` 처럼).

## 3. 기본적인 사용 방법
고급 사용자가 아니면 다음과 같이 사용하면 됩니다.

1. `template` 폴더를 복사한다
2. data 폴더에 원하는 데이터를 넣는다
3. `index.vl.json` 파일을 수정한다. 특히 data url을 2번에서 넣은 데이터로 변경한다
4. `index.html`파일은 웹브라우저로 실행하거나 새로고침해서 시각화 결과 확인

코드를 수정할때마다 새로고침 하는 것이 귀찮으면 VSCode Extension인 `Live Server`를 설치한 뒤 html파일을 우클릭해서 `Open with Live Server`를 클릭하면 됩니다. 그럼 파일이 변경된 것이 감지되면 자동으로 새로고침을 수행합니다.