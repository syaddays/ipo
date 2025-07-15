from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import IPO
from .serializers import IPOSerializer

# API Views
class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = IPO.objects.all()
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset

# Template Views
class IPOListView(ListView):
    model = IPO
    template_name = 'core/ipo_list.html'
    context_object_name = 'ipos'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming'] = IPO.objects.filter(status='upcoming').count()
        context['open'] = IPO.objects.filter(status='open').count()
        context['closed'] = IPO.objects.filter(status='closed').count()
        context['listed'] = IPO.objects.filter(status='listed').count()
        return context

class IPODetailView(DetailView):
    model = IPO
    template_name = 'core/ipo_detail.html'
    context_object_name = 'ipo'
