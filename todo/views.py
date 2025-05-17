from django.shortcuts import HttpResponse

def task_create(request):
    html_response = """
    <form>
        <label for="name">Vazifa nomi:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="desc">Tavsif:</label>
        <textarea name="desc" rows="10" cols="30"></textarea><br><br>
        <label for="due_date">Muddati</label>
        <input type="date" id="due_date"><br><br>
        <label for="priority">Muhimlik darajasi:</label>
        <select id="priority" name="priority">
          <option value="past">Past</option>
          <option value="orta">O'rta</option>
          <option value="yuqori">Yuqori</option>
        </select><br><br>
        <button type="submit">Vazifani saqlash</button>
    </form>
    """
    return HttpResponse(html_response)
