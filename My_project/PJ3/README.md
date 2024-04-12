# 선택한 프로젝트
ver2 영화 
# 하고자 한 것
최대한 Django의 기능을 많이 써보려고 한점

# 어려움을 겪은 부분
해결한 코드
```
{% for file, title, content in movie_arr %}
      <div class="card mt-3 m-2" style="width: 18rem;">
        <div >
          <img src="{% static file %}" alt="movie{{forloop.counter}}" class='card-img-top' style = 'height:50vh'>
        </div>
        <div class="card-body">
          <h5 class="card-title">{{title}}</h5>
          <p class="card-text">{{content}}</p>
        </div>
      </div>
    {% endfor %}
```
1. for 문으로 나오는 forloop.counter 을 static 태그안에 넣어서 `이미지 파일 + 숫자 + .jpg`로 이미지 주소를 가져오려고했음
   ```
   {% for i in data %}
    <div class="card" style="width: 18rem;">
      <img src="{% static 'images/movie'|add:forloop.counter|add:'.jpg' %}" class="card-img-top" alt="movie{{forloop.counter}}">
    </div>
  {% endfor %}
   ```
   하지만 
   1. `|add` 필터를 사용해서 붙이니 `static/.jpg` 까지만 나왔고
   2. `|add{{forloop.counter}}`을 하니 syntax 에러가 발생했고
   3. `|add'{{forloop.counter}}`을 하니 `static/images/{{forloop.counter}}.jpg`라고 인식했음
   =>
   그래서 view.py 함수에서 `파일 이름`으로 구성한 리스트를 만들어서 templates로 넘겨줘서 for의 인자로서 static에 넣어서 해결함
### 또한.
`[파일명,영화제목,영화설명]` 으로 이루어진 리스트를 만들어서 넘겨줬음 => 데이터베이스를 활용하는 듯한 방법으로 처리함

# Community 페이지 처리 하는 방법
996px를 기준으로 안의 구성이 바뀜
container를 두개를 만들고 
하나는 996px일떄 `d-none`을 줘서 안보이게 했다가 996px가 넘는 순간 `d-block`요소를 줘서 보이게 했고,
다른 하나는 반대로 적용해서 넘는 순간에 교환이 되도록 처리했음
