How names work
--------------

1. name can be defined as
      - start with _, $
        - _: 의도적으로 private하다고 지칭하는 장치이다.
        - $: 코드 생성기나 전처리, 변환컴파일러를 위한 것으로 추가된 사양이다. 따라서 그것은 프로그램에서 건들지 않는 것을 전제로 하기 때문에 당신이 프로그램이 아니라면 $는 그냥 두길 바란다.
      - ends with _, &, digits

2. js의 names는 소문자 영어 표현으로 시작해야 한다.
   이것은 왜냐하면, js의 new연산자 때문인데, new연산자로 시작하는 것은 constructor함수를 호출하는데 이 constructor와 delegating과 일반함수를 구분하기 위해서이다.

   자바스크립트는 내부적으로 constructor함수와 일반함수에 구분할 수 있는 도구를 전혀 사용하지 않고 있기 때문에 사용자가 이를 구분하기 위해서 신경 써야하고 그것은 에러를 줄이는데 큰 도움을 줄 것이다.

   나의 해결방법은 간단하다. new를 사용하지 않는 것. 이것은 우리가 대문자를 변수명의 새로운 규칙으로 추가할 수 있도록 한다.


3. 자바스크립트에 예약된 이름은 아래와 같다.

.. code-block: javascript

    arguments, await, break, case, catch, class, const, continue, debugger, default, delete, do ,else, enum, eval, extends false, finally, for, function, if ,implements, import, in, Infinity, instanceof, interface, let, NaN, new, null, package, private, protected, public, return, static, super, switch, this, throw, true, try, typeof, undefine, var, while, with, yield


