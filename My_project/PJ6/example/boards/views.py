from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Board, Comment
from .forms import BoardForm, CommentForm
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET"])
def index(request):
    # django 에서 실제 DB 요청은 데이터를 실제로 사용할 때 가져온다
    # 지연 로딩 (lazy loading)
    # 중복된 sql 문을 방지하고, 효율적으로 관리하기 위해
    boards = Board.objects.all().order_by('-created_at')
    
    # 게시글이 현재 10개가 저장되어 있다.
    # 하지만 11번 발생
    # N + 1 problem 발생
    # for board in boards:
    #     print(board.comment_set.all())

    # 어떻게 해결할까?
    # 키워드 : 즉시 로딩 (Eager loading)
    # 1. annotate -> count, avg
    # 2. select)related -> 정참조 시에 발생하는 중복 쿼리 해결
    # 3. prefetch_related -> 여참조 시에 발생하는 중복 쿼리 해결
    context = {
        'boards': boards
    }
    return render(request, 'boards/index.html', context)

@require_http_methods(["GET", "POST"])
def detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')

    comments = board.comments.all()
    comment_form = CommentForm()
    
    context = {
        'board': board,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'boards/detail.html', context)

@require_http_methods(["GET", "POST"])
def update(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm(instance=board)
    context = {
        'board': board,
        'form': form,
    }        
    return render(request, 'boards/update.html', context)

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = BoardForm()
    context = {
        'form': form,
    }
    return render(request, 'boards/create.html', context)

@require_http_methods(["POST"])
def comment(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.save()
            return redirect('boards:detail', board.pk)

@require_http_methods(["POST"])
def comment_detail(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('boards:detail', board_pk)