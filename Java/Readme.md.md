# Java Basic
# OOP
 - Encapsulation(은닉화), Inheritance(상속), Polymorphism(다형성)
# Encapsulation 은닉화
하나의 클래스 안에 데이터와 기능을 담아 정의하고, 중요한 데이터나 복잡한 기능 등은 숨기고, 외부에서 사용에 필요한 기능만을 공개하는 것
+하면 public : 외부에서 바로 접근이 되버림 
-하면 private 라고 대체로 정해짐 : 외부에서 직접접근 불가 => getXxx, setXxx 으로 접근한다
### Pirvate 와 Public 차이 : Scope와 관련해서 명시해주기
Python의 LEGB : 로컬, 엔클로징, 글로벌, 빌트 인
private = 로컬
public = 글로벌
# Inheritance 상속
객체 정의 시 기존에 존재하는 객체의 속성과 기능을 상속받아 정의하는 것
- ### Generalization
	- 추출된 class의 공통적인 특성의 모아 super class로 정의할 수 있다,
- ### Specializtion
	- 비슷한 속성과 기능을 가지고 있는 다른 class를 상속 받아 새로운 class를 정의할 수 있다.
class 설계 시 특정 class를 상속 받아 그 class의 Data(변수)와 기능(method)를 사용할 수 있게 한다.
```
java.lang,Object 
	java.util.QAbstractCollection<E> 
			java.util.AbstractList<E> 
				java.util.ArrayList<E>
```
- is a 관계
	- MainCustomer is a Customer
- 상속 되어지는 클래스의 속성이나 기능을 선택적으로 상속 받을 수는 없다.
- 상속을 받게 되면 super 클래스의 모든 속성과 기능을 상속받아, 사용할 수 있게 된다.
	- pricate 정의된 super의 member는 상속은 되어 지지만 접근할 수는 없다.
	- super의 constructor는 sub 클래스의 constructor내의 첫 라인에 super()로만 접근이 가능하다.
- 상속 받은 기능 중 수정을 원하는 기능은 다시 재정의(Overriding)할 수 있고, 필요한 속성이나 기능은 추가하여 작성할 수 있다.
- Java 에서는 class의 상속을 단지 하나만 받도록 제한한다.
	- 객체지향의 다른 언어에서 다중 상속으로 인한 문제점이 발견
	- single inheritance
	- 다중 상속의 이점을 위해 interface를 제공한다.
- sub 객체 생성 시 super도 같이 생성된다.
- MainCustomer mc = new MainCustomer();
### super
- 현재 수행중인 객체가 상속받은 객체의 참조값을 갖는 reference variable
- 객체 생성시 자동으로 생성된다.   
	- super.memberVariable : 현재 수행중인 객체의 member variable과 상속받은 super 객체의 member variable 이름이 같을 경우 사용
	- super.method() : 상속받은 메소드 호출 시, 현재 수행중인 객체와 상속받은 객체의 메소드명이 같을 경우 사용
	- super (parameter_list) : parameter_list와 같은 super 객체의 constructor를 호출한다.
	  단. constructor 내의 첫 라인에서만 사용가능, this()랑은 같이 사용 못함!!
### Overriding
반드시 상속관계까 있어야된다. => 상속관계가 있을 때 재정의하는 것
상속받은 super의 method 중 특정 method의 내용을 수정, 추가하여 정의하는 기법
- sub 클래스의 Overriding되는 method는 상속받은 super 클래스와 아래 내용이 반드시 같아야 한다.
	- Name
	- Return type(Java 5.0에서 SubClass 가능)
	- Argument list
- Access modifier는 같거나 보다 넓은 범위를 가져야 한다.
	- suepr가 public 이다? 자식은 무조건 public 될 수 밖에...  private는 상속이 안돼...
### Overriding 과 Overloading의 공통점/차이점
- method 정의 시 사용되는 기법
- method 이름을 같게 정의
- Polymorphism(다형성) 효과
- Overriding : 
		- 상속을 기반
		- super 부터 상속받은 기능 중 특정 기능을 재정의하는 기법
		- return_type, ==method이름, parameter_list는 항상 같게==
		- access modifier는 같거나 보다 넓은 범위로 정의
- Overloading:
	- 하나의 클래스나, 상속받은 클래스의 내에
	   같거나 비슷한 기능의 method의 이름을 같게 정의해서 편리성을 추구
	- ==method 이름은 같게, parameter_list는 다르게== 정의
	- 나머지method 형식은 상관 없다.
### 자주 Override되는 java.lang.Object 의 method
- toString()
	- 객체를 문자열로 표현하는 메서드
	- toString 메서드를 재정의하여 System.out.println() 메서드 등에 활용
- equals()
	- 두 객체가 같은지를 비교하는 메서드
	- equals 메서드 구현부에 특정 조건을 만족하는 경우를 두 객체가 같다고 재정의하여 비교문에 활용
- hashCode()
	- 객체의 해시 코드: 시스템에서 객체를 구별하기 위해 사용되는 정수 값
	- HashSet, HashMap 등에서 객체의 동일성을 확인하기 위해 사용
	- hash가 ==다르면 다른것,== hash가 같으면 같을수도 =="있는 것"==
	- ** equals 메서드를 override할 때는 hashCode도 override하도록 권장함
		미리 작성된 String이나 Number 등에서 재정의된 hashCode 활용 권장
# Polymorphism 다형성
같은 타입 또는 같은 기능의 호출로 다양한 효과를 가져오는 것
- 하나의 이름으로 여러 개의 형태를 구성할 수 있는 OOP 특징
- Java의 가장 강력한 특징
- Type Polymorphism (Object Polymorphism)
	- 같은 타입의 변수가 다양한 형태의 객체를 참조하는 것
	- super type의 변수가 다양한 sub type을 참조하는 형태
	  ex) ```Parent p = new Child();```

- Method Polymorphism
	- 같은 클래스 타입은 같은 mehod를 호출 시 그 기능이 다양하게 처리되어지는 것
	- 메서드 호출 시 VM는 그 메서드가 Overrideing 되어 있는지 여부를 확인하고, 생성된 객체의 xxx 막 Overriding 된 메서드를  호출한다.
	- sub 객체 생성시 super 도 같이 생성되어지기 때문에 memmory에 존재하는 super type으로 변수를 선언할 수 있다.
	- Customer cc = new MainCustomer();
	  System.out.println(cc); 를 호출하면, MainCustomer의 toString()이 호출된다.
		- MainCustomer()가 구현하고 있는 toString()이 불린다.
```
		class PolyTest{
			public static void main(String[] args){
			System.out.println(c);

			MainCustomer mc = new MainCustomer("소나무", "부산", 21, "여행");
			System.out.println(mc);

			Customer cc  = new MainCustomer("강나루", "인천", 25, "게임);
			System.out.println(cc);
			}
		}
```
### Reference 자동(묵시적) 형변환
`SuperType var = sub객체;`
주의) 
	- super가 가지고 있는 member만 사용 가능하다
	  var.memberVariable 또는 var.memberMethod() 사용 시 (Compiler check)
	- var.memberMethod() 사용시 compiler는 super에 가지고 있는지를 체크하지만, 실행(runtime) 시엔 overriding 되어 있는 method가 있다면 overriding된 method를 수행한다.
### Reference 명시적 형변화
`SubType ver = (SubType) superType변수;` ==타입 캐스팅 해서 넣어야 된다!!!==
```
Customer cc = new Customer(); //1
...
if ( cc instanceof MainCustomer){
	MainCustomer c = (MainCustomer) cc; //2
	...//객체 처리
}
```
> [!NOTE]  instanceof
>  - 전달되어온 변수의 객체 타입이 무엇인지를 정확하게 확인하여 작업하고자 할 때에는 instanceof 연산자를 이용한다.
> - 어떤 객체의 인스턴스 인지를 확인 후 casting 하여야 견고한 프로그램을 작성할 수 있다.
> - ```
> 	public void compute(Customer customer){
> 	if (customer instanceof MainCustomer){
> 		MainCustomer mc = (MainCustomer) customer;
> 		System.out.println("주요고객에 대한 처리 수행..."+ mc.getName() + " 취미:" + mc.getHobby());}
> 	else{
> 		System.out.println("고객에 대한 처리 수행..." + customer.getName());
> 	}} ```


# Abstraction 추상화
현실 세계에 존재하는 객체의 주요 특징을 추출하는 과정
### ==구현부가 없는 메서드가 왜 필요할까?==
=> 상속받아 쓰기 위해? ==컴파일러를 통과하기 위해==
컴파일러가 하는 일 : 있는지 여부를 확인하는 것
```java
Parent p = new Child();
만약 같은 변수나 메서드가 있다? 문제 X (컴파일러가 부모한테 이런 메서드가 있구나 하고 넘어가고
			 => 런타임 진행하면서 부모->자식 순서로 상속이 이루어지면서 자식의 메서드가 나옴)
But 자식에만 있다? 문제 발생 ( 컴파일러가 없는데?????? 하면서 에러발생 하면서 런타임까지 안감)
```

```java
class Parent(){
	void mParent(){
		System.out.println("parent emethod);
	}
}
class Child() extends Parent{
	void mChild(){
		System.out.println("child emethod);
	}
}
...
Parent pp = new Parent() // 이건 됨
Parent p  = new Child();
p.mchild(); // 이건 안됨						
```
<->
```java
abstract class Parent(){
	void mParent(){
		System.out.println("parentt emethod);
	}
	abstract void mChild();
}

...

Parent p = new Parent(); // 컴파일러 단계에서 안됨
p.mChild() // 이건 됨						   
```
### abstract 
- 일부 구현되지 않은 메서드를 포함할 수 있는 클래스
- 객체 지향이란? 존재하지 않은 것을 가져다가 쓰는 것 
- 예를 들어 "운송 수단"이라는 개념을 abstract로 만들어 놓고
	비행기, 승용차, 트럭 등등이 이 운송수단이라는 것을 상속받아 쓰는 것
	운송수단 [] : 
	[0] = new Truck()
	[1] = new 비행기()
	...
> [!NOTE] 객체를 생성하지 못함
> - 완전히 구현되지 않았기 때문
>- 상속을 주어서 상속 받은 클래스가 abstract 메소드를 구현해야 사용 가능
>	- Overriding
>- Sub 클래스 객체 생성 시 super type으로 사용 가능
>- ==ClassName() 이 안됨, 근데 ClassName [] class_name = new ClassName[5]; 는 가능==
>- => 오브젝트(객체)생성이 안될 뿐 데이터 타입으로는 쓸 수 있다.
# Interface
- 상수(final)와 구현되지 않은(abstract) 메소드로만 구성
- 특별히 정의하지 않아도 컴파일 시에 아래 제한자가 추가된다.
	- public static final 제한자가 상수 앞에 붙는다
	- public abstract 제한자가 메소드 앞에 붙는다.
		--> Overriding 시 항상 public 제한자를 가져야 한다. 
```java
interface Trans{
	abstract void start(); // 동일 : public abstract void start();
	void stop(); // 동일: public abstract void stop();
}
```
### default method
-  java 8 버전부터 body를 갖는 method를 추가할 수 있음
 ```java
interface Trans{
	...
	default public void doTrans(){
		System.out.println("default method")
	}
}
```
자바는 단일상속만 가능하다
=> 한계를 극복하기 위해 인터페이스 만들어짐
=> 인터페이스는 ==다중구현(상속)==이 가능하다.
> [!NOTE]  interface
> - 인터페이스는 객체 생성 할 수 없다
> 	- 구현되지 않은 메서드를 포함하기 때문
> - super type으로 사용
> 	- 상속되어져서 sub class가 구현되지 않은 모든 메소드 구현 -Overriding
> 	- 상속한  sub class들의 명세서 역할로 사용
> 	- Polymorphism 효과
> - interface는 다른 interface를 다중상속 할 수 있다.

# Nested class
클래스 안에 클래스
- class 안에 다시 정의 되는 class를 말함
- 바깥 class의 일부처럼 사용되고, 바깥 class의 member에 접근할 수 있다.
```java
class Outer {
	public boid outerMetthod(){
		System.out.println("outerMethod()..........");
		Inneer invar = new Inner();
		invar.innerMethod();
	}
	class Inner {
		void innerMethod(){
			System.out.println("innerMethod().....")
		}
	}
	public static void main(String[] args){
		Outter ou = new Outer();
		ou.outerMethod();
	}
}
```
### anoymous inner class
- 이름없이 만들어지는 class
- Android에서 Event 처리에 자주 활용되는 방식
```java
public class AnonymousInner{
	public Folder gotNewFolder(){
		return new Folder(){
			public void open() {}
			public void fold(){}
		};
	}
}
interface Folder{
	public void open();
	public void fold();
}
```

```java
public class AnonymousInner{
	public Folder gotNewFolder(){
		class TempClass implements Folder{
			public void open() {}
			public void fold(){}
		}
		return new TempClass();
	}
}
interface Folder{
	public void open();
	public void fold();
}
```
### static inner class
- class안에 다시 정의되는 class를 말함
- 별도의 객체 없이 사용할 수 있음
```java
public class StaticInner{
	public void outerMethod(){
		System.out.println("outerMethod()....");
	}

	public static class Inner {
		public static void innerStaticMethod(){
			System.out.println("innerStaticMethod().....");
		}	
		void innerMethod(){
			System.out.println("innerMethod().....");
		}
	}
}

public static void main(String[] args){
	StaticInner.Inner innerStaticMethod(); // static method call
	StaticInner.Inner in = new StaticInner.Inner();
	in.innerMethod();
}

// 출력 값
innerStaticMethod()............
innerMethod()..........
```
# Collection
- Java는 객체지향 언어이다.
- 수많은 객체를 생성하고, 이동해야 할 경우 객체를 임시저장 할 객체가 필요
- java.util : package에 객체들을 저장하고 관리할 interface와 class 정의
- Collection : 모든 클래스들의 객체를 요소(element)로 저장하는 객체들의 최상위 interface
> 가장 초기에 ArrayList만 있었다. 
> --> 이 ArrayList에는 다양한 걸 넣게 될꺼니까 넣을 때마다 타입캐스팅를 진행해야겠다 
> --> 근데 실제 개발로 들어가니까, 결국 넣던 타입만 넣게 된다.
> --> 계속 똑같은 것을 넣는 데 항상 타입캐스팅을 해야되네?
> --> Generic 등장
## Generic
- Collection은 다양한 형태의 Object를 담으려는 목적으로 만들어졌으나, 대부분이 동일한(특정한) Object들을 담는 용도로 사용됨
- 담을 클래스를 특정하기 위해서 추가됨
- Java 1.5 부터는 Generic ( <> )을 도입해서, Class Code 작성 시점에 임의의 (가령 <T>) 타이을 사용하도록 하고, 그 Class 를 사용하는 Code 에서 <T> 대신 실제 사용하는 Type (가령 <String> )을 사용할 수 있도록 하였음
	- public class 클래스명<T> {...}
	- public interface 인터페이스명<T>{...}
	- T : reference ==T==ype, E : ==E==lement, K: ==K==ey, V: ==V==alue
	- 선언부의 data type과 생성부의 data type은 반드시 같아야 함
		- 클래스명<String> 변수 = new 클래스명<String>();
		- 클래스명<String> 변수 = new 클래스명<>();

# Design Patten
정답은 아니지만, 하나의 가이드라인이 될 수 있음
### 싱글톤? 
현실에 하나만 존재하는걸 메모리 상에도 하나만 존재하게 강제화 하는 것(new 를 한번만 하게 하는 것) / new 할때마다 계속 새로 생길 수는 없으니...
어떻게? 
1. 생성자를 private로 만든다. (싱글톤의 첫 번째 조건)
```java
// singleton 의 첫번 째 !
private static EmployeeMgr instance;

public static EmployMgr getInstance(){
	if(instance ==null){
		instance = new EmployeeMgr();}
	}
	return instance
} 
// 가져다 쓸 때
EmplyeeMgr mgr = EmployeeMgr.getInstance();
EmplyeeMgr mgr1 = EmployeeMgr.getInstance();
EmplyeeMgr mgr2 = EmployeeMgr.getInstance();
// 세 개의 객체가 바라보는 인스턴스는 동일 하다.
````
# Java IO
