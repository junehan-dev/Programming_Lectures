Name Rules
----------

1. name can be defined as
      - start with _, $ - _: 의도적으로 private하다고 지칭하는 장치이다.
        - $: 코드 생성기나 전처리, 변환컴파일러를 위한 것으로 추가된 사양이다. 따라서 그것은 프로그램에서 건들지 않는 것을 전제로 하기 때문에 당신이 프로그램이 아니라면 $는 그냥 두길 바란다.
      - ends with _, &, digits

2. js의 names는 소문자 영어 표현으로 시작해야 한다.

   ::

      이것은 왜냐하면, js의 new연산자 때문인데, new연산자로 시작하는 것은 constructor함수를 호출하는데 이 constructor와 delegating과 일반함수를 구분하기 위해서이다.

      자바스크립트는 내부적으로 constructor함수와 일반함수에 구분할 수 있는 도구를 전혀 사용하지 않고 있기 때문에 사용자가 이를 구분하기 위해서 신경 써야하고 그것은 에러를 줄이는데 큰 도움을 줄 것이다.

      나의 해결방법은 간단하다. new를 사용하지 않는 것. 이것은 우리가 대문자를 변수명의 새로운 규칙으로 추가할 수 있도록 한다.


3. 자바스크립트에 예약된 이름은 아래와 같다.

.. code-block:: javascript

   arguments
   await
   break
   case
   catch
   class
   const
   continue
   debugger
   default
   delete
   do
   else
   enum
   eval
   extends 
   lse
   finally
   for
   function
   if
   implements
   import
   in
   Infinity
   instanceof
   interface
   let
   NaN
   new
   null
   package
   private
   protected
   public
   return
   static
   super
   switch
   this
   throw
   true
   try
   typeof
   undefine
   var
   while
   with
   yield


Declaration
-----------

::

   JS는 3가지 Statements들이 변수 선언에 사용된다.( ``let, function, const``\)
   그리고 쓸모없는 statement가 있는데, ``var``\,이고 그것은 사랑받지 못한 브라우저인 IE의 것이다.

let
^^^

let에 대해 이야기 해보자.

::

   let선언은 현재 scope에서 새로운 variable를 선언한다.
   모든 block은 scope를 생성한다.
   let선언들은 또한 initialize를 허용하지만 필수로하지는 않는다.

   let 선언은 또한 destructuring을 허용한다.
   desctructuring은 중요한 기능은 아니지만 일부 패턴을 개선할 수 있다.

functions
^^^^^^^^^

::

   function <name> 선언은 기본적으로 let을 전제한다.
   ``let test = undefined; test = function test(){run();}`` 

   모든 함수들은 hoistede된다.
   이 부분들은 당신이 배치한 곳에서 제거되고 body혹은 module의 최 상단으로 재배치 된다.
   모든 함수 정의로 생성된 let선언들은 최상단으로 이동한다.

   이것이 function들이 block내부에 위치하지 말아야 하는 이유이다.
   함수선언을 body나 모듈에 놓는 것이 좋지만, 함수선언을 if, while, switch같은 구문에 넣는 것은 좋지 않다.


const
^^^^^

::

   이는 let과 비슷하지만 2가지점에서 큰 차이가 있다.

   1. initialization이 필수.
   2. 변수는 이후에 재할당 된 수 없다.

   만약에 선택을 할 수 있는 상태라면, 나는 const사용을 선호한다.
   왜냐하면 이것은 더욱 커다란 깨끗함을 강조하고 나아가도록 도와주기 때문이다.

datatypes
---------

number
^^^^^^

   js의 number는 기본적으로 IEEE의 float-point숫자를 사용한다.

   ::

      자바스크립트의 숫자타입이 하나만 있기 때문에 거대한 이점을 가진다.
      프로그래머들은 그들이 어떤 타입을 정하기 위해 혹은 타입을 추측하기 위해 타입변환을 신경 쓸 필요가 없다. 
      하지만 자비스크립트는 IEEE754표준을 그대로 쓰지는 않는다.
      java의 subset을 사용하는데, java double고 매우 밀접한 관련이 있다.
      64비트 길이의 floating point type이다.
      숫자는 sign비트를 포함하고 11개의 지수부와 53개의 가수부를 지닌다. 

      가수부는 가장 뒤쪽에 위치하게 되는데, 0.5 <= significand < 1.0사이의 값을 가진다.
      이 형식 안에서 항상 1의 값을 가진 비트로 시작하기 때문에, 따로 표시하지 않고 1bit를 보너스로 사용한다.

      위의 1비트를 항상 1을 둔다는 가정하에 보너스비트를 취하기 때문에, zero는 없어야하지만 zero가 있다. IEEE 754 표준에서 0, -0이 동시에 존재하기 떄문에,
      ``(1/0) === (1 / -0) // false`` 가 된다.
      
