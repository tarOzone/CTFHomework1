
ans = "_iamhurting"
ans_curr_idx = len(ans)


def rotate_ans():
    global ans_curr_idx
    ans_curr = ans[ans_curr_idx % len(ans)]
    ans_curr_idx += 1
    return ans_curr


title = "Little Birdie"


body = """
Oh, little birdie
Up there in the tree,
Do I see you?
Is it you who sees me?
.
If I was to leap from my window-sill,
Dive through leaf and twig, breath held,
Just to clutch you in my palm,
To hear your soft feathers flutter...
.
Would I feel you?
Would you feel me?
.
If you flew to my shoulder,
Your wings spread wide with majesty,
A crimson vessel, darting from your perch,
To seek my unworthy touch...
.
Would I find you?
Would you find me?
.
What if I seized you,
Squeezed you in my fist,
To feel you tremble.
To feel you quake...
.
Would I harm you?
Would you harm me?
.
What if you attacked me,
Claws out, just to combat me,
Focused, tense, and ready.
Like an apex predator...
.
Would I hurt you?
Would you hurt me?
.
But it isn't that simple.
I stare at my birdie,
With regret ringing in my ears,
A knife in my heart.
.
It lays in my hand,
As dead as the night sky.
And the tree is empty,
And its branches are bare.
.
It falls to the pan,
Sinking deep into the water,
Its beauty torn away
By my ravaging hands.
.
The meal is soon ready.
I take painful chews,
With stinging tears
Pouring down my cheeks.
.
And I look down at my meal,
And I wish, how I wish,
We could've met in a different life,
And we could've been friends.
.
Oh little birdie,
Who lived in the tree,
Did I kill you?
Was it you who killed me?
""".split('\n')
