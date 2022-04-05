Primitive object and container object
-------------------------------------

.. code-block:: javascript

   [1,2,3] == [1,2,3] // false
   [1,2,3] === [1,2,3] // false
   assert.deepequal([1,2,3], [1,2,3]) // true
   assert.equal([1,2,3], [1,2,3]) // false

- 기본적으로 모든 데이터는 immutable이라고 가정하고 접근하는게 착오를 줄일 수 있다.
- const는 namespace에 대한 불변성을 보호하는 장치이고 값을 변경하는 것은 불가능하다.
- array, object는 value object라기 보다 reference collection object로 구분하는 게 좋다.
- collection object는 object collection이기 때문에 자체의 container로서의 구분만 있을 뿐 값이 존재하지 않는다.
- 그러면 왜 자바스크립트는 object에 대한 값을 불변으로 처리할까?
- 이게 싫었다면 그냥 객체지향언어가 아니도록 설계를 했어야했을까?
- 대부분 개발자들은 프로그램의 메모리에 민감한데 왜 자바스크립트는 이렇게 처리를 했을까?
   - 누구나 쉽게 사용할 수 있도록 하여야 해서?
   - object 원형에서 instance를 추적하여 GC를 수행하기 때문에?
   - 왜 메모리에 접근해서 값을 바꾸지 않나?
   - 그렇다면 instance를 추적해서 해당 reference에서 값을 저장하는 부분에 수정하면 되지 않을까?
   - 아마 불가능한일은 전혀 아니었을거라고 생각이 들지만, 메모리관리자가 존재하는 상황에서, 값을 변경해서 메모리 재할당이 일어날 경우 track해야하는 reference가 변경되는 상황이 생길수록 메모리 누수가능성이 높아지는, 그리고 자바스크립트의 사용성상(초보자의 사용, 정지하지 않는 프로그램) 그런식으로 수행하면 재할당과 파편화가 반복되어서 결론적으로는 오히려 메모리를 비효율적으로 사용하여서 이렇게 설계된게 아닐까 생각이 든다.


annonymous function to arrow function
-------------------------------------

고급 언어 레벨에서 익명함수(lambda expression)를 메모리 효율적인 방식으로, namespace를 소모하지 않고 함수를 콜백으로 사용하는 패턴이 유행하면서 function토큰을 소모하지 않고 좀 더 간편하게 사용할 수 있는 arrow function을 만들어준 덕분에 기존 자바스크립트의 익명함수를 간편하게 처리할 수 있게 되었다.

.. code-block:: javascript 

   alert((function(x){
      return x * x;
   })(10));

   alert( ((x) => x*x))(10) );

This context의 변화
^^^^^^^^^^^^^^^^^^

arrow function은 또한 this 스코프를 최상위 수준으로 끌어올린다.

.. code-block:: javascript

   let outer = {
      "name" : "out hi!",
      "inner" : {
         "name": "inner hi",
         a() {
            console.log(this.name);
         },
         'b' : () => {
            console.log(this.name, this);
         },
         'c' : function (){
               (() => {
                  console.log(this.name);
               })()
         },
      },

   }

   outer.inner.a(); // inner hi
   outer.inner.b(); // undefined 
   outer.__proto__.name = "OBJECT hi";
   outer.inner.b(); // Object hi
   outer.inner.c(); // inner hi

JS의 클래스
----------

.. code-block:: javascript

   class Person {
      constructor(name, age) {
         this.name = name;
         this.age = age;
      }
      speak() {
         console.log(this.name);
      }
         
   }

   let person = function (n, v) {
      this.name = n;
      this.age = n;
   }

   person.prototype.speak = () => {
      console.log(this.name);
   }


   a = new Person("class", 20);
   b = new Person("prototype", 20);

   a.speak();
   b.speak();

class 인터페이스가 생겨 기존의 class기반 객체지향언어의 표현과 통일하였지만, 구현은 기존과 다르지 않다.

- getter와 setter가 constructor호출 이전에 bind되는점이 다른 언어오 차이가 있다. 따라서 아래와 같이 동적프로퍼티 할당을 


