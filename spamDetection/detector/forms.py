from django import forms

class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Enter your message here....'}))
    #Hi John,
#Just a reminder that we have a meeting scheduled tomorrow at 10 AM.
#Let me know if you need anything before then.
#Thanks,
#Sarah”

#congratulation you have won a lottery