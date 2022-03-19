---
title: "숫자시스템과 10진수"
date: 2022-03-19T00:36:47+09:00
categories:
- STUDY
tags:
- number
#thumbnailImage: 
---

요약
----

> 10에 기반을 두고 있는 수체계 혹은 십진수(decimal)는  
아주 자의적으로 이루어졌다고 할 수 있겠다고 합니다.
>
> 제가 챕터에서 파악한 결론은 십진수에 숫자(digit)이라는 것은 도구이고  
십진수는 그것들중 하나 일뿐 중요하게 받아들여야 하는 것은 numeric 시스템이라고 저자는 말하고 있다고 생각합니다.

> >  {{< figure src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Two_hand%2C_ten_fingers.jpg/220px-Two_hand%2C_ten_fingers.jpg" title="십진수의 기원" >}}

> 숫자는 일반적인 bases기반에 대해서 가장 높은 추상화수준을 가졌다고 합니다.
> > {{< figure src="/media/1.png" title="" >}}
> > {{< figure src="/media/2.png" title="" >}}
> (Tally marks, 필요한 만큼 선을 긋는 걸로 수를 표한하는 방식으로 구성요소도 unary 1개이다)
> > {{< figure src="/media/3.png" title="" >}}
> 로마자(V(5) 와 V(5) 를 더하면 *X*(10)이 된다.)

> > {{< figure src="/media/4.png" title="" >}}
- 0과 10의 등장으로 숫자는 숫자끼리 조합되고 연결될 수 있었으며 사실 중요한 것은 혹은 더 추대받아야할 것은 숫자를 표현하는 기호(0-9)보다 이 시스템이 중요하다고 합니다.

___
- 십진수 시스템 이전의 숫자들은 표현이 차지하는 부피나 비용이 제한적이었면 십진수에서 가장 주목할 부분은 *10*기호보다 0에 있습니다.

> 이 시스템은 이전의 그 어떤 숫자 시스템과도 차원이 다르다.
> > {{< figure src="/media/6.png" title="" >}}
- 우측처럼 0을 나열하는 것만으로도 숫자는 새로운 의미를 가지고,  
또한 좌측처럼 지수표현으로 정리되어도 규칙을 깨뜨리지 않습니다.

> > {{< figure src="/media/5.png" title="" >}}
> 10의 제곱수를 표현할 때에도 그저 1의 자리를 옮기고 0을 자리지킴이(placeholder)로 배치하는 것으로 의미가 완성되기 때문에 특별한 기호가 필요하지 않습니다.

> > {{< figure src="/media/4.5.png" title="" >}}

numeral system
--------------

- References,
  https://en.wikipedia.org/wiki/Numeral_system 

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Numeral_Systems_of_the_World.svg/264px-Numeral_Systems_of_the_World.svg.png" title="numbers!" >}}

> 10진수 시스템에서 가장 우아한 것은 positional system이다.  
> 이는 place-value 표현식으로 알려져 있다.  

> 연산 또한 위치기반 시스템에서는 더욱 쉽다.
> > 더하는 기능은 더 큰 숫자의 다른 기호들로 10의 승수를 표현해야 하지만, 위치기반 시스템 그럴 필요가 없다.


positional notation system
--------------------------


- References,
  https://en.wikipedia.org/wiki/Positional_notation

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Positional_notation_glossary-en.svg/300px-Positional_notation_glossary-en.svg.png" title="" >}}

> positional시스템은 힌두-아라비안 숫자시스템의 다른 어떤 수를 기반하더라도 이동하는 것으로 기능하는 시스템입니다.
> 더 일반적으로 말하면 숫자를 이동한다는 것은, 그 위치에 대응하는 값에 의해서 자동으로 곱한다는 것입니다. position*index
