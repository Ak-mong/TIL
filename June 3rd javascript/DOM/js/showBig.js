var bigPic = document.querySelector("#cup");
var smallPics = document.querySelectorAll(".small"); //작은 이미지를 노드리스트로 가져옴

for (var i=0;i<smallPics.length; i++){
    smallPics[i].addEventListener("click", changePic);
}

function changePic(){
    var newPic =this.src; //click이벤트가 발생한 대상의 src 속성
    bigPic.setAttribute("src", newPic); 
}



// var isOpen = false;
// var bigPic =document.querySelector("#cup");
// var smallPics = document.querySelectorAll('.small'); //작은 이미지를 노드리스트로 가져옴

// for (var i=0;i<smallPics.length; i++){
//     smallPics[i].addEventListener("click",
//     function(){
//         var newPic = this.src; // click이벤트가 발생한 대상의 src속성
//         bigPic.setAttribute("src", newPic);
//     });
// }
 
// var view = document.querySelector('#view');
// view.addEventListener("click",function(){
//     if (isOpen == false){ // 상세정보가 안보임 -> 보이게 처리
//         document.querySelector("#detail").style.display = "block";
//         view.innerHTML = "상세 설명 닫기";
//         isOpen = true;
//     }
//     else{ // 상세보기가 보임 -> 안 보이게 처리
//         document.querySelector("#detail").style.display = "none";
//         view.innerHTML = "상세 설명 보기";
//         isOpen = false;
//     }
// });

