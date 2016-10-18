import csv
with open('output.csv', 'w') as outputFile:
    writer = csv.writer(outputFile, delimiter=',') #delimiter = '\t'
    writer.writerow(["Artist", "Title", "Lyrics"])

    artist = "Unter Null"
    title = "Godless"
    song = """
    So many days I can't stop myself
    From fighting this monster that eats me alive
    So many times I've fought and I've tried
    To live for a moment without fearing my mind
    I hate this, yet live this, and it's bringing me down
    I feel like I'm standing on uneven ground
    The balance to life has been skewered so violent
    I'm so sick of this death-instinct silence

    So despondent and so somber, so frail
    So scared to begin for the fear I will fail
    I'm alone in this pattern and I can't call for grace
    I'm left in this mess that is such a disgrace
    I fear for my mind more than I fear for life
    The one thing worth saving is the love I deny
    For I feel so hollow, and I yearn to relent
    The control for some peace and freedom from this torment

    There's no one to save me and I can't save myself
    I would give my whole being for some kind of help
    But no one can stop this god damn monster so great
    All hope is now lost and it's too late
    I numb to forget, to quiet the noise
    I'm deafened by silence, I can't live with myself
    I numb to forgive, for myself can't forget
    That I could've been someone without any regret

    You lying man who tells a tale
    Of flawless love and peace of mind,
    Of parting seas and curing blind
    Your lies my faith, there's no remorse
    You spin your tale with brutal force
    Your lies, my faith, my breathing grace
    I ran from life, I erased my faith
    I am so blind
    And seeing eyes are not the kind
    """
    writer.writerow([artist, title, song])
