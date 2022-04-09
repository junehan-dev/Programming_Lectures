02 defer, async and strict mode
--------------------------------

``async``
   고전적인 스크립트에게 만약 async속성이 존재한다면, 고전적인 스크립트는 병렬적으로 Fectch reqeust를 수행하고, parsed, evaluated된다.
   모듈 스크립트에 있어서 async속성은 그의 의존성들은 모두 다른 queue에서 실행된다. 그러므로 그들 또한 병렬적인 실행시간을 가지게 된다.
   이 속성은 브라우저의 parser-blocking js를 제거할 수 있다. 브라우저가 단계적인 처리의 IO WAIT를 기다리지 않아도 되는데 이 경우는 defer와 비슷한 효과를 갖는다.

``defer``
   이 boolean속성은 브라우저에게 해당 스크립트가 document parse이후헤 execution을 희망한다고 지시한다. 하지만 이것은 ``DOMContentLoaded`` 이전의 것이다.

   ``defer`` 속성은 document에서 그들이 읽어 진 이후에 실행된다.
   이 속성은 async와 마찬가지로, 브라우저의 Parser-blocking js를 제거할 수 있다. async와 동일한 병렬처리에 포함되지만, 해당 문서의실행(evaluation)시점을 언제로 두는지에 대한 차이가 있다.


``strict``
   strict mode는 ES5에 소개되었고, 내부적으로 sloppy mode를 제거하는것으로 변칙성의 자바스크립트를 제한함으로 허용하지 않는다.
   이것은 단순히 Subset이 아니다. 내부적으로 normal mode가 사용하는 semantics 혹은 token parse가 다르다.
   strict모드는 아래에서 기본 Semantics와 차이가 있다.

      1. js의 조용한 에러제거하고 throw에러 방식으로 변경한다.
      2. js 엔진이 최적화하기 어렵게 만들었던 실수들을 고쳤다.
      3. 미래의 예정된 ECMA사양에 포함된 syntax를 금지한다.

   Strict모드는 기존 자바스크립트가 수행할 수 있었던 허용중 대표적으로 아래와 같은 것들을 제한한다.

   - TypeError
      - ``var undefined = 5;, var Infinity = 5``
      - ``var obj2 = { get x() {return 17;} }; obj2.x = 4;``
      - ``delete Object.prototype``
   
01 What is Javascript 
---------------------

Why 
^^^

   - Programmable한 document, Document사용에 대한 기능을 추가하기 위한 것인데 기존 doucment를 읽는 브라우저는 동작을 잘 하고 있었기 때문에, 굳이 document를 읽은 프로그램이 document를 생성하기 보다, document는 그대로 두고 그 위에서 동작하는 script language를 염두해 둔 것으로 보여진다.

Til ES6
^^^^^^^

   - ES1(1997) ~ ES4(2000) 3년간 variable, function, operator, input, output에서 errorhandling에 대한 명세까지 처리할 수 있는 수준으로 안정화된다.
   - 브라우저마저 언어표현의 표준이 달랐지만 인터넷 사용률은 컴퓨터 보급이 증가함에 따라 개발자들도 증가하게 되어, 이 언어를 다루는 개발자들이 커뮤니티를 형성하면서, jquery, dojo 같은 프레임웤이 크로스 브라우징을 처리해주는 역할로 등장하게 되었다. (jquery를 사용하면 jquery가 브라우저에 fit한 표현으로 골라서 변경해주는 방식)
   - IE가 대세를 이루었던 시점에 google의 크롬이 등장하면서, 느슨했던 IE의 동작보다 당연히 더 좋은 성능의 브라우저를 사람들이 사용하게 되면서, IE의 독자적인 방식에서 전체 브라우저 표준으로 방향이 전환되게 된다.(ES5)
   - ES5까지는 prototype기반으로만 객체지향 object를 생성할 수 있었지만, javascript가 수행하는 기능이 youtube, online game, utility on web, community graphics등 도메인도 다양해지고 데이터, 기능이 넘쳐흐르면서, javascript는 한번더 프로그래밍 언어로서 조금 더 느슨함을 벗어던지고 프로그래밍 언어답게 keyword를 제공할 필요를 가지게 되었는데,
  - ES6에서 class, variable type(let, const), generator, decorator등이 등장하면서, 좀 더 편리하게 패턴과 일반적인 인터페이스로 프로그래밍이 가능해졌다.

Whats more
^^^^^^^^^^

   - javascript가 사실상 전세계 사용률 1위의 언어가 되었기 때문에, 해당 표준 엔진인 v8엔진을 기반으로 webbrowser뿐만 아니라, mobile의 환경, 그리고 backend service까지 구성할 수 있는 node, angular, react등이 등장하고 superset인 ts까지 설계되어 앞으로 더욱 세상의 변화에 민감하게 반응하고, 적응할 수 있는 최고의 언어로 살아남게 될 것이라고 추측된다.


추가 과제
--------

for in for of
^^^^^^^^^^^^^

   - for in과 for of 모두 객체에 포함되는 속성을 이용하여 for loop를 사용할 수 있습니다. 표현의 간소함과 효율적인 방식으로 일반적으로 많이 사용하는 패턴인 연속적인 데이터를 순차적으로 1회씩 이라는 절차를 위해 만들어 주었습니다. for in 의 경우 Object.keys()로 조회하면 얻게되는 array의 index, object의 속성키등을 대상으로 순회를 하는 반면, Object.values()로 얻을 수 있는 대상에서는 대부분 for of를 사용할 수 있습니다. 단적으로 array iterator generator등이 대상인데, 값을 순차적으로 추출하는 것이 논리적으로 맞다 라고 판단되는 객체를 대상으로 Object.values를 수행할 수 있고, iterator, generator같은 경우는 전체가 물질화 되지 않은 상태로 값들을 loop당 한번씩 추출하기 때문에 대용량데이터 처리시에 이점이 있습니다.


Put vs Patch vs Post
^^^^^^^^^^^^^^^^^^^^

HTTP PUT METHOD (1.1)
   자원의 생성, 교체에 사용되면 full updates에만 사용됩니다.

HTTP PATCH METHOD (2010)
   full update의 대신 부분적인 업데이트로 새로운 자원을 생성하기 위해 만들어 졌습니다.

Put과 Patch사이의 가장 큰 차이는 Put의 경우 요청URI를 사용하여 원본의 버전을 대체할 수정된 버전을 제공하는 반면 Patch의 경우 원본을 수정하기 위한 명령의 집합을 사용하여 자원을 수정합니다.
   
