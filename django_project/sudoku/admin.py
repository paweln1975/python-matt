from django.contrib import admin
from .models import SudokuPuzzle, SolvingAttempt

@admin.register(SudokuPuzzle)
class SudokuPuzzleAdmin(admin.ModelAdmin):
    list_display = ('id', 'difficulty', 'created_at', 'solved')
    list_filter = ('difficulty', 'solved')
    ordering = ('-created_at',)

@admin.register(SolvingAttempt)
class SolvingAttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'puzzle', 'started_at', 'is_completed')
    list_filter = ('is_completed',)