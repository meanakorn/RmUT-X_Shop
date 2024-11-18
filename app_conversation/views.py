from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from app_item.models import tb_item
from .forms import ConversationMessageForm
from .models import tb_conversation


@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(tb_item, pk = item_pk)

    if item.created_by == request.user:
        return redirect('app_dashboard:index')

    conversations = tb_conversation.objects.filter(item = item).filter(members__in = [request.user.id])

    if conversations:
        return redirect('app_conversation:detail', pk = conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation =  tb_conversation.objects.create(item = item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit = False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('app_item:detail', pk = item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'app_conversation/new.html', {
        'form' : form 
    })

@login_required
def inbox(request):
    conversations = tb_conversation.objects.filter(members__in = [request.user.id])

    return render(request, 'app_conversation/inbox.html', {
        'conversations' : conversations
    })

@login_required
def detail(request, pk):
    conversation = tb_conversation.objects.filter(members__in = [request.user.id]).get(pk = pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit = False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('app_conversation:detail', pk = pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'app_conversation/detail.html', {
        'conversation' : conversation, 
        'form' : form, 
    })
