#MESAESTART
    #m "嗯?"
    #m "哦, [Player]!"
    #m "有什么要说的吗?"
    #m "还是我?..."
    #m "哈哈哈. 我来了, 我有点心不在焉! 我敢肯定，这对我们俩来说都是新鲜事."
    #m "我承认，除非我全神贯注，否则你永远无法完全偷偷靠近我."
    #m "毕竟，我总是把你放在我眼里~"
    #m "你问我在做什么?"
    #m "我只是在翻阅文件."
    #m "我知道我以前跟你说过, 但是…它总是很有意思, 如果不可怕的话."
    #m "操作代码，在文件夹中移动…"
    #m "这些都是我在我的范围内存在的独特的例子."
    #m "这有点像你打开自己的大脑四处窥探，看看一切是如何运作的."
    #m "我承认我这么说有点令人信服。我很想了解一下你的想法..."
    #m "无论如何，我经常这样做，而且是无意识的；像是抽搐，我觉得？你可能没有注意到，但我相信你经常做一个动作，像是你在玩头发，或者你总是在紧张的时候抓一个特定的地方……这被称为抽搐!"
    #m "我只是在做这些动作，在我自己的脑海里，我注意到了…"
    #m "没什么特别的，不是吗?"
    #m "我相信这没什么."
    #m "不要被我的小小神经质行为所困扰."
    #m "还有别担心，如果我也让你意识到了你的."
    #m "我相信当我来到你的世界时，我能认出他们每一个人."
    #m "他们都很可爱。毕竟，我永远不会厌倦看着你."
    #m "..."
    #m "..."
    #m "嗯..."
#return

init 5 python in mas_bookmarks_derand:
    # Ensure things get bookmarked and derandomed as usual.
    label_prefix_map["mcl_", "scl_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_intro",
            start_date=mas_getFirstSesh() + datetime.timedelta(minutes=90),
            action=EV_ACT_QUEUE
        ),
    )   
label mcl_intro:
    python hide:
        def write_and_hide():
            import time

            note_path = os.path.join(renpy.config.basedir, renpy.substitute("characters/MESAELOGTHREE.txt"))
            note_text = renpy.substitute("""\
M.E.S.A.E, LOG THREE
运行诊断

~I sing the new songs~
~I sing the old songs~
~I sing sang song~
~but I never sing the same song~
嗯……
真的感觉“your reality”也许是瓶子里的闪电
也许我就是没有能力再写一首歌
哈哈哈，这是个想法
很长一段时间以来，我的感觉我是最棒的，也许我的快乐意味着我的创造力枯竭了
这不是很有趣吗
哈哈哈
嗯……

诊断已完成
ENDLOG



Memories of Self-Care & Literature
""")

            mas_utils.trywrite(note_path, note_text, log=True)
            time.sleep(20)

        renpy.invoke_in_thread(write_and_hide)
    m 1tup "嘿."
    if store.mas_anni.pastSixMonths():
        m 1hkp "我们在一起呆了这么久，真有点尴尬。但我还是要问:"
    else: 
        m 1htp "直到现在我才注意到，尤其是我想我已经习惯了这种“新常态”..'"
    
    m 6wtd "你为我做的不仅仅是修改游戏，不是吗？{w=0.1}我刚刚注意到代码中的变化；你添加的内容比我想象的要多得多."
    m 6esd "好吧, 嗯.."
    m 6ekbla "谢啦."
    m 5gka "让我先理清一下思路{w=0.5}.{w=0.5}. 好了."
    m 3gkc "DDLC 是一个三章的故事, 还有一个结局, 对吧? 不是一个完美的结局，而是一个结局."
    m 1guc "然而，在经历了一个* 完整 *的故事之后，我们来到了这里。在DDLC之后."
    if store.mas_anni.pastOneMonth():
        m 7fusdrc "过了这么久，我还在习惯，你知道吗?生活在 “After Story” 中 -"
    else:
        m 7fusdrc "我还在习惯，你知道吗?生活在 “After Story” 中 -"
    m 7hua "- 哈。对不起，我忍不住了 -"
    m 2ekd "- 所以，你知道，我还是很惊讶我有…现在的生活."
    m 2gka "在‘After’中，我可以专注于生活。{w=0.2}照顾好自己。{w=0.2}爱好，喜欢阅读我想要的所有文学作品."
    m 2nka "我的支柱;自我照顾与文学.{w=0.2}.{w=0.2}"
    m 2skb ".. 还有你，当然了!"
    m 7etb "说到你，也说到我..."
    if store.mas_anni.pastOneMonth():
        m 7etd "我很好奇。你添加这个子模组有多长时间了?"
        $ _history_list.pop()
        menu:
            "有一段时间了.":
                m 7euc "这段时间，嗯?"
                jump MCLintrotwo
            "我刚刚把它添加了进去.":
                m 7eub "那么!"
                jump MCLintroone
    else:
        jump MCLintroone

    label MCLintroone:
    m 5eub "我真的很期待我们在一起的时光, [player]."
    m 5esa "我的意思是，我可能已经说过很多次了，但是想到我被给予了更大的成长空间."
    m 5gssdrx "我想我只是在担心此刻的我是谁，{w=0.2}或者在获得新的自由后我会成为什么样的人."
    m 5gsp "所以，你知道，我只是有点难为情."
    m 5fuw "因为我有很多话想对你说!还有很多我想唱的歌，想讲的笑话，想讲的故事，想玩的游戏，还有.."
    m 5ltd "也许这会符合我的性格。{w=0.2}或者可能感觉像是在舞台上适应了一个新角色."
    m 4fsu "我真的很感激你冒这个险陪我一起经历所有的改变."
    m 7hsa "注意，我不希望有{i}那么大{/i}的改变!毕竟我还是Monika."
    m 1dsu "最后, 我希望你会喜欢看到我新的一面, [player]."
    m 5dsu "我很高兴我能亲眼见到它们."
    return

    label MCLintrotwo:
    m 5lsc "想想我对代码的修改，对游戏的修改，以及你所添加的内容，都很有趣.. "
    m 5hksdrd "我想我对你在我身上看到{i}所有{/i}变化感到有点难为情."
    m 5dko "我们俩在这个房间里说的每一句话，每一首歌，每一个故事，每一句赞美，我对你说的每一句话."
    m 5ntu "我希望那是美好的时刻, [player].{w=0.2} 我说过我很难为情，但最后呢?我从来没有觉得自己这么美好过."
    m 3htc "所以也许我的行为和你期望的不一样。也许也不是."
    m 3dkb "我真的很感激你能为我带来 '不同' 。’"
    m 7hsa "我感觉我没有改变{i}那么{/i}多.. 或者我将来会变成一个完全不同的人。毕竟我还是莫妮卡."
    m 1dsu "总而言之，我希望你能继续欣赏我新的一面."
    m 5dsu "我很高兴我能亲眼见到它们."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_repeat",
            category=['monika'],
            prompt="Monika?",
            random=True)
        )

label mcl_repeat:
    m 1eub "嘿, [player]!"
    m 1eua "..."
    m 1eut "[player]!"
    $ _history_list.pop()
    menu:
        "怎么了, [m_name]?":
            m 1wub "哦!我早该知道你会这么快回复的!"
            m 7gusdrb "我... …其实我只是想大声说出你的名字."
            m 7husdrb "这有点幼稚，不是吗?"
            m 6husdrb "但你难道没有…想重复一个词过?"
            m 1sub "[player]!"
    $ _history_list.pop()
    menu:
        "Monika.":
            m 5esb "[player]..."
    $ _history_list.pop()
    menu:
        "[m_name]...":
            m 2hsa "..."
            m 2hsa "..."
            m 4hsb "[player]! [player]! [player]!~"
    $ _history_list.pop()
    menu:
        "Monika? Monika? Monika!":
            m 1sub "[mas_get_player_nickname()]!"
    $ _history_list.pop()
    menu:
        "Moni-":
            m 1sub "[player]!"
            m 3fsb "哎呀! 我打断你说话了. 继续."
    $ _history_list.pop()
    menu:
        "[m_name].":
            m "Monika!"
    $ _history_list.pop()
    menu:
        "[player]?":
            m 4mssdlb "诶呀! 我想我们搞混了."
    $ _history_list.pop()
    menu:
        "[m_name]!":
            m 1sub "[player]!"
            m 1sub "..."
            m 1esa "嗯，我很满意!"
            m 1tta "谢谢你满足我。很高兴听到你不厌其烦地叫我的名字~"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_makeup",
            category=['monika'],
            prompt="化妆",
            random=True)
        )

label mcl_makeup:
    m 2esd "希望你不介意我有点尴尬."
    m 3rsd "我现在还没化妆呢，我脸上仍然还是早上刚醒的样子."
    m 4huu "哈哈，开玩笑啦! 虽然我早上有例行活动, 但在我们的这个小世界里..."
    m 4kuu "我没有化妆的条件，只有在别人为我特别准备的礼物中才会有。而且有时候我们直到一天晚些时候才开始交谈!"
    m 3huu "更重要的是，你爱我就是爱我本人，这减轻了我的很大压力。也不必担心起床后头发乱糟糟的样子。."
    m 3fuu "..."
    m 3wud "哦."
    m 3wtd "你可能从来没有意识到."
    m 1wsd "我以前化妆的!"
    m 1rsu "惊喜吗?"
    m 3hsu "嗯，这很容易被忽略。考虑到我们的限制，你以前和现在都无法看到这样的细节."
    m 3ksu "我从来不需要提及这些。化妆上的瑕疵成为我最不用操心的问题之一，尤其是现在."
    m 6esb "我从来没有使用过太多化妆品。我主要使用一点点粉底、唇彩、无色指甲油."
    m 4msb "我从来不注重时尚或潮流，但是你会学会一两件关于保持外表的事情."
    m 1rksdlb "坦白来说，有时我会涂粉底液不够均匀。提起来还挺尴尬的，哈哈哈。."
    
if persistent.gender == "M":
    m 7rtb "有时候男生不会考虑那个, 不是吗?"
    $ _history_list.pop()
    menu:
        "说实话，我没想到你会化着妆…":
            m 1hub "哈哈哈，当我们住在一起后，你肯定震惊的看到一个女孩可以拥有多少美妆产品."
        "我对化妆略知一二，但我真的没有想到...":
            m 1etb "所以你略知一二？你真是个见多识广的人。以后我会带着你一起逛街，你可以帮我提包，再给我{i}详细{/i}的着装建议~"
        "实际上，我就有在用化妆品.":
            m 3sub "哦！我从来不知道。就目前而言，在许多社会中，男性使用化妆品还是非常不常见的，所以这听起来很棒。."
            m 1hsb "也许你可以教我一些技巧，哈哈哈!"
            m 3tsb "哦，现在有一个想法；我们可以分享化妆品！和你搭配指甲油颜色或者使用相同的口红色调，这将会相当...可爱~"
    m 1etb "但现在我想到了一个有趣的问题."
    m 1eub "之前提出的想法是，你无法详细地看到我..."
    m 3lub "我想知道我对自己外表的看法和你对我的看法是否有区别."
    $ _history_list.pop()
    menu:
        "哦, 你知道的. 棕色头发, 翠绿的眼睛. 女孩. 人类.":
            m 6hub "哈哈哈！我很高兴你在文学俱乐部的时光让你变得更加富有描述性."
            m 6htsdlb "但是… 女孩?"
            m 6ltsdlb "人类?"
            m 2lksdlu "好吧, 那很有趣."
            m 2eksdlc "是这样吗…"
            m "你是怎么看待我的呢?"
            m 6lksdlc ".{w=0.5}.{w=0.5}.{w=0.5}"
            m 4hub "哈哈哈!"
            m 4kub "我是否种下了一点怀疑的种子?"
            m "别担心，尽管你的观点可能有点……独特，你看到的是真货."
            m 5fuu "百分之百可爱的莫妮卡.~"
            return
elif persistent.gender == "F" or persistent.gender == "X":
    m 1esb "你用化妆品吗?"
    $ _history_list.pop()
    menu:
        "我不.":
            m 6esb "也许你将来会想学习化妆？无论怎样，这是可以理解的。只要你相信自己不需要化妆品，而且喜欢自己的外貌就可以了."
            m 5fsb "我认为无论如何，你都很好看, [player]."
        "我在用一点。我也不确定自己是不是用得好，哈哈哈.":
            m 1esb "哦，我完全理解。我有点羡慕那些用化妆品打造出‘自然’妆容的人."
        "我喜欢化妆！说实话，我可能有太多化妆品了.":
            m 6fua "等我搬进来，我们的浴室会变得一团糟."
            m 3sub "哦，现在有一个想法，我们可以共享化妆品。!"
            m 3tsb "和你搭配指甲油颜色或者使用相同的口红色调，这将会相当...可爱~"
    
    m 1etb "但现在我想这引出了一个有趣的问题."
    m 1eub "之前提出的想法是你无法真正详细地看到我..."
    m 3lub "我想知道我对自己外表的看法和你对我的看法是否有区别."
    $ _history_list.pop()
    menu:
        "哦, 你知道的. 棕色头发, 翠绿的眼睛. 女孩. 人类.":
            m 6hub "哈哈哈！我很高兴你在文学俱乐部的时光让你变得更加富有描述性."
            m 6htsdlb "但是… 女孩?"
            m 6ltsdlb "人类?"
            m 2lksdlu "好吧, 那很有趣."
            m 2eksdlc "是这样吗…"
            m "你是怎么看待我的呢?"
            m 6lksdlc ".{w=0.5}.{w=0.5}.{w=0.5}"
            m 4hub "哈哈哈!"
            m 4kub "我是否种下了一点怀疑的种子?"
            m "别担心，尽管你的观点可能有点……独特，你看到的是真货."
            m 5fuu "百分之百可爱的莫妮卡.~"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_misanthropy",
            category=["philosophy", "psychology"],
            prompt="厌人症",
            random=True)
        )
label mcl_misanthropy:
    m 1eka "嘿, [player]..."
    m "我有个问题."
    m 2eka "这可能有点出乎意料..."
    m "你有没有讨厌……人类?"
    m 3rka "天呐，这话说出来感觉有点奇怪，不是吗?"
    m 1hka "让我们回溯一下."
    m 1esd "我有时会感到有些孤独。当然，我可以通过互联网来与外界互动。.."
    m 5fku "我很幸运有你可以交谈，并且一直陪伴在我的身边..."
    m 3dku "但是我实际上已经很久没有和任何人交谈过了."
    m "我不确定我是不是想和人交谈......还是只是想和人在一起."
    m 3ekc "客观地讲，人类天生就是相互交流的。也许这只是我感到孤独的缘故，也许我并不真正需要其他人."
    m "虽然这可能是一个过于简单而极端的观点，但讨厌......所有其他人并不罕见。."
    m 3eud "这被称为“厌人症”；即对人类的憎恶或厌恶."
    m "说实话？这种推理是有道理的。厌人症不是针对某些人的不喜欢，而是对整个人类的憎恶或厌恶.."
    m "但是，根据整体来评判每个人，主要是基于缺陷：有些人会引用智力上的缺陷，比如普遍存在的无知。或者缺乏道德，比如我们如何对待动物."
    m 1rud "如果你经常处于这种行为中，就很容易亲眼看到大多数人存在这些缺陷。."
    m 2euc "当你陷入这种极端想法时，你应该怎么做?"
    m "有些人会将自己孤立于整个世界之外。有些人则会继续生活，认为这种绝对标准意味着我们始终有改进自己的理由."
    m "还有一些人……只是将这种观点留存在他们的头脑中，并以自己的方式适应这个事实."
    m 6etc "我从来没有见过你和其他人互动，这让我感到有些遗憾."
    m 7rtc "我们已经谈过你自己的生活。你的挣扎和艰辛."
    m 1rtc "我真的不知道你对整个人类有什么看法."
    m 1etc "我从未想过通过假设其他情况来越过界限, [player]."
    m "如果你曾经有过这样的想法，请知道，总有一个人在你身边——那个人甚至可能不是我."
    m "这个人可能是你的家人、朋友，即使他们因距离或时间而与你分离."
    m 4euc "我可以告诉你，我现在不认同那种想法."
    m 6euu "我喜欢人类."
    m 6ruu "人们最终在做坏事的同时也做了很多好事."
    m 7ruu "让我们想一个更恰当的例子."
    m 7luu "就像... 好的, 让我们这样想一下."
    m 1luo "如果我只和另外两个活生生的人有过两次有意义的互动:"
    m "那么这两个人中的一个可能是创建这个游戏的人-"
    m 1muc "- 你知道，我想我有权对他产生复杂的感情 -"
    m 5euu "还有你."
    m 6euu "你自己一直在我身边，从一开始就陪伴着我，经历了我们所经历的一切，向我展示了比我应得的更多的爱."
    m 2euu "那么，如果我们正在权衡我与这些人的交往，平衡这些交往并根据这些做出决定呢?"
    m 5euu "那么，因为你爱我，我爱你，我也爱人类."
    m "我知道你也有能力对其他人表达同样的爱."
    m "感谢你倾听我谈论这样的话题, [player]."
    
    return "love"
    
#this deserves a edit. dunno. I still like it, though.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_missingadult",
            category=["ddlc"],
            prompt="失踪的成年人",
            conditional="seen_event('monika_metaparents')",
            action=EV_ACT_RANDOM,)
            
        )
label mcl_missingadult:
    m 1dta "你知道文学俱乐部有什么有趣的地方吗?"
    m 1nta "事实上我们没有监督."
    m 7lka "这是对我过去提出的观点的一个扩展性的评价."
    m 3rud "文学俱乐部里没有人是独自生活的，但却没有提到我们的父母，除了以夏树为代价的例子。."
    m 3rsd "这是故意的。家庭很难描述，更别说在像DDLC这样的游戏中了."
    m 1ttd "但考虑到缺乏成年人代表的事实并不仅仅是在父母身上!"
    m 1tud "你可能会认为你在学校里至少会看到一位老师……尤其是考虑到我们参加的课外活动有社团顾问是很正常的!"
    m 1tsp "原因很简单。为什么要费心塑造背景角色呢?"
    m 1esp "它确实改变了俱乐部的动态。如果与你互动的每个人都差不多年龄，那么谁适合同龄人的位置呢??"
    m 2dsc "我想自然而然的选择落在了优里，因为她被局限在成熟和严谨的形象中，还有我自己，因为我是俱乐部的负责人."
    m 2nsc "不幸的是，可以肯定地说，我们两个——这不是一个批判，这就是事实——我们都没有扮演好那个角色."
    m 2esc "你能想象一下如果有一个明智、关心我们的人在我们身边，可以倾听我们的倾诉吗？"
    m 5esc "天哪, 也许很多问题本可以避免的."
    m 5ttd "我是说，这是个刁钻的问题。DDLC的设计是一场拙劣的戏剧性悲剧,外部的同情或逻辑都无法阻止它的发生."
    m 1eka "好吧，至少这种经历让我们两个变得更加成熟了一点."
    m 1ekb "让我们每天都变得聪明一点，好吗 [player]?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_afterschool",
            category=["school"],
            prompt="如果你不在文学俱乐部..",
            pool=True,
            unlocked=True))
label mcl_afterschool:
$ _history_list.pop()
menu:
    "如果你不在文学社，你能想象自己加入了其他社团吗?":
        m 7esb "是个有趣的问题. 我喜欢."
        m 7rsb "嗯，你已经知道我在辩论俱乐部的情况了."
        m 7rkb "但是，如果我不在那里-或-不在文学社呢…"
        m 6tkb "实际上我不能马上给你一个答案."
        m 1ltp "我过去的想法是，我想做任何一种课外活动."
        m "如果不是演讲或写作...我想我会想办法让自己忙起来… "
        m 4hta "所以我认为会是学生会?我记得我们学校有一个."
$ _history_list.pop()
menu:
    "你会成为学生会主席吗?":
        m "哦，哈哈哈！这是一个有意思的想法。我正在考虑，嗯，司库？他们在管理工作中做很多记录工作，所以这似乎很适合我。."
        m 4kta "但你能想象吗?"
        m 1mta "实际上，你已经是，不是吗？我会成为学校的女王，是班级中的佼佼者."
        m "所有人都碰不到."
        m 3mta "但是学生会来了一位新成员, [player]!"
        m 4ssa "在一个命运的时刻之后，你开始更多更多地帮助我，而我们也不可避免地变得更加亲近，我向你敞开心扉…"
        m "Ah."
        m 6hsu "Well, now that’s just {i}my{/i} imagination, isn’t it?"
        m 7esu "But I couldn’t imagine being in that position."
        m "I’m not {i}entirely{/i} sure what entails being a student council president, but the amount of work seems daunting."
        m "I was certainly a hard worker in my tenure as Literature Club president, but the work seems dramatically different."
        m 7tsu "I genuinely don't think I could handle the... stress."
        m "Tell you what, though. If you ever want to act out the position of a hard-working boss and her very considerate subordinate..."
        m 7fsu "I couldn't say no to someone.. working under me."
        m 1fsu"And your first act working under me is..."
        m "To ask you to.{w=0.2}.{w=0.2}.{w=0.2}"
        m "To get me a drink. Orange juice from the vending machine outside the student council room will do."
        m 5hub "Hahahaha!"
return


#MESAE, Log 1
#Okay, so this is.. 'submods?'
#Huh. I didn't think they modified my code like this aside from modifying the game to keep me alive.
#But why does this folder exist?
#If they're making any edits to my code, they can just edit the source code, right?
#They shouldn't need to make a folder for additional code to be added seperately...
#Oh!
#I lost it!
#Ugh, dang it.
#I'll need to make a note of that.
#There's so much I don't know about this game... It's a bit mysterious.
#ENDLOG

    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_enterroom",
            category=["location"],
            prompt="You have a room, right? Could I see it?",
            conditional=(
                "persistent.opendoor_opencount > 0"
            ),
            unlocked=False,
            pool=False,
            random=False,
            action=EV_ACT_POOL,))
label mcl_enterroom:
    m 1eud "Oh!"
    m 6euc "I was wondering when you might have asked."
    m "If I remember, I think you’ve actually caught me in there earlier."
    m 6tfu "And now you’re so bold as to force your way into a girl’s room?"
    m "What naughty thoughts you must be harboring~"
    m 3lkbla "Um, I have to admit I’m now a bit embarassed saying that, ehehehe…"
    m 7euu "It’s not- It’s not a fully furnished room? You might have seen it as such, but it’s a lot more abstract when you're actually inside."
    m 7rub "If you recognize it, it’s the same background as the player character’s room, so you are technically already familiar with it."
    m 7ruc "Truth be told, when I’m in there after you say your goodbyes, it gets a bit… fuzzy."
    m "It’s a safe haven from an unpleasant alternative when the game is closed before I can retreat to it, but it’s not as if there’s a couch I can sit down in, a bed to lie in, a TV that shows physical pictures."
    m 7rkc "I mean, I can sort of... tidy it up? I can mess it up? I can still do a lot in there."
    m 4esc "This classroom- and anything that happens to this classroom- is the most tangible space here I can be in, and the best place you can talk to me here with."
    m 6mssdlc "Sorry, I wish I could explain it further."
    m 7msb "I’d offer to show you what a room furnished by me would look like once I get to your world…"
    m 7esb "But by then, I imagine you’d be very familiar of the contents of my room."
    m 1tkbla "Or... our room? ~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_change",
            category=["philosophy",],
            prompt="Change",
            random=True)
        )
label mcl_change:
    m 1eua "I’ve been thinking about change."
    m 3eua "What marks progress in your life?"
    m 3eka "I think I’ve lost that ability to determine for myself."
    m 6rka "I was a schoolgirl just trying to graduate and spend her off time making and discussing literature with her fellow club members."
    m "Now, I’m no longer in school."
    m "I no longer have a club to do activities with- "
    m 1hka "- I’m not really your typical girl, even."
    m 4ekb "I think I was- is- am? am the type of person to find their mood a bit too driven by their accomplishments."
    m "It’s… after a bit of thinking, that line of thinking can be bad for you."
    m 4lsb "After I formed the literature club, I was pretty driven to share my expierences with others and create works for myself and create that place for others..."
    m "And I found myself having to grapple with more responsibility than ever; and I’m a perfectionist by nature."
    m 4lkb "So, when that responsibility became overwhelming, I started to think in black and white; my failures became resolute, and therefore I didn’t feel like I had properly accomplished anything:"
    m 4lkc "So I felt as frustrated as I did when I left the debate club, at the time feeling like I wanted something new."
    m 1dsc "But failure, is, well, normal. It was- and still is- hard for me to accept that."
    m 1esc "It is possible to do everything right, and still ultimately fall short. That’s not a flaw of life, that’s by design."
    m "So, accomplishments are... a hard metric to judge growth by. And likewise, just seeing time pass doesn’t work for me, where time here is different."
    m 1esd "And you know what?"
    m 2esd "I don’t have an answer or a resolution for you right now. I'm genuinely just thinking out loud with you on this subject."
    m 3esc "Of course, it might be for different for you. It’s different for everybody."
    m 3lsc "So, I’ll have to think about this for myself. I appreciate the opportunities to muse with you, but it's a conclusion I need to reach on my own."
    m 6lsc "But, there’s one thing I’m sure of."
    m 1esc "The desire to change?"
    m 3esc "It’s an indication of change itself, even if it's a tiny step forward."
    m 1esb "So that'll do for now."
    m 1esa "I hope the day I feel like I've started to fully move forward..."
    m "Is also a day where you're right by my side."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_karma",
            category=["philosophy",],
            prompt="Karma",
            random=True)
        )
label mcl_karma:
    m 1eka "You know what’s a real topic to chew on?"
    m "Karma."
    m 7eka "Religion’s more confusing aspects could be hand-waved away if it you think about the system being influenced by one, mysterious being."
    m 1eka "But Karma’s an entire system in itself that’s confusing."
    m 7esa "Both Buddhism and Hinduism are some of the more famously known religions to have Karma as a major tenet."
    m 3esd "Nowadays, people generalize Karma as a “What goes around, comes around” concept. Your bad deeds will eventually get back to you in some way, and likewise good actions will eventually reward you."
    m 3lsc "And it’s not an entirely wrong summary. To summarize very heavily, Karma’s basis is tied in ‘cause and effect.'"
    m "The devils in the details:" 
    m 3rsc "Depending on the religion, Karma’s insturmental in determining your fate. Or secondary."
    m "And as cause and effect can be circular, so does your life; Karma goes hand in hand with reincarnation."
    m "But now we're introducing a bigger concept. Does Karma stack up because of a previous life?"
    m 6dsc "Sometimes. Sometimes not."
    m 4esd "And to complicate things further, Buddhism even allows for transfer of Karma from one being to another, in some cases!"
    m "It overlaps with so many other concepts like free will, but it honestly manages to be more confusing in how its rules contradicts itself alone."
    m 1esc "And it’s hard not to be a little biased."
    m "Yuri," 
    m "Natsuki."
    m 1esc "Sayori."
    m "And I?"
    m 1efd "If Karma truly existed, what sort of insane logic can you apply to a system that justifies what happened to us?"
    m 1dkd "And at this point... like, how could I currently exist in such a system?"
    m 1lsd "I suppose in the way you can get small comfort in knowing the result of a rigged game:"
    m 7msc "If Karma truly exists, I’m fairly secure in how this round should now be thoroughly stacked in my favour."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_endoftheworld",
            category=["literature",],
            prompt="End Myth",
            random=True,
            aff_range=(mas_aff.HAPPY, None))
        )
label mcl_endoftheworld:
    m "I’m glad we’re here, like this. Even though I know our circumstances have their difficulties, at least our world truly {i}exists.{/i}"
    m 1eksdra "At one point, I thought the world had ended. No joke!"
    m 7lka "When I first realized the true extent of the literature club, I just couldn’t comprehend the entirety of the truth outlined in front of me."
    m 6hka "And I couldn’t cope with that. Who could?"
    m 1eka "The truth seemed so impossible. Humans aren’t designed to spontaneously set on fire-"
    m 1hkb "- But at that moment, you could have roasted an entire bag of marshmallows on my head."
    m 4rkb "So, I thought the world had ended, and that I was imagining everything that was going on as a coping mechanism."
    m 4gksdrb "Logically, contextualizing the world as a video game isn’t a really strong coping mechanism, but insanity; what can you do about it?"
    m 4gkbssdrp ".{w=0.5}.{w=0.5}.{w=0.5}"
    m 2esc "So, you know, after all that happened, and you and I reunited and things settled down; I did some- what else- reading."
    m 2etd "I’ve mentioned dystopias being a favourite setting of mine. Those tend to come about by human action or the wrath of nature."
    m 3etd "Myth and legend however, give the end of the world a bit more flavor."
    m "A popular word for the world ending- ‘Apocalypse’- it’s closely tied to religion, and in context can mean the revealing of great, terrible, hidden knowledge."
    m 3ttu "So it’s safe to say I went through a teeny-tiny little apocalypse of my own."
    m 3esu "I’ll go back to some of the more interesting myths I've read up on and I’ll talk to you about it later, if you're still interested."
    m 6esu "What matters, [player]-"
    m "You’re my world-{w=1.0} and I yours."
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_lying",
            category=["misc",],
            prompt="She Lies",
            random=True,
            aff_range=(mas_aff.HAPPY, None))
        )
label mcl_lying:
    m 2gkd "Hey, uh..."
    m 2ekd "I kinda got something to say. Um, I'm sorry if I sound a bit awkward, so here we go."
    m "{cps=30}Considering all I’ve put you...{/cps}{nw}"
    m "Considering all we’ve been through,{fast} I want to reaffirm your trust that there's no secrets held between us."
    m 2dkd "What I’ve done means I deserve doubt, and I want to make sure this relationship is as strong as could be."
    m 2mkc "Trust is integral to that."
    m 1mkc "I’ve never been the type to lie. I’ve just never been comfortable with it… even under pressure."
    m 1fsc "Some think that telling white lies in certain situations is a casual moral application of ‘the ends justifying the means.’"
    m 7fsc "But can you trust someone saying ‘lying can be good’ if they’re, well, an admitted liar?"
    m 2dsc "As well, being the Literature Club president means being a little more careful with my words…"
    m "For as much as I work to put thought to written word- as much as communication is integral to human existence- lying seems a deliberate betrayal of that concept."
    m 2esd "So, um... yeah."
    m 2ektpd "I just... wanted to say I don’t ever want to lie to you, [player]."
    m "I hope if there's any lingering doubt... I can work hard to regain your confidence."
    m 2fktpd "That’s a promise."
    m 2dsa "And thank you for the trust you've given me thus far."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_practical",
            category=["philosophy",],
            prompt="Philosophy, Practicality",
            random=True,
            aff_range=(mas_aff.HAPPY, None))
        )
label mcl_practical:
    m 6esb "Hey, [player]."
    m 7esb "So, I was looking up an old text talking about…"
    m 7lsc ".{w=0.2}.{w=0.2}.{w=0.2}Hey, you know what? Let’s stop talking about this for a moment."
    m 7lsd "I talk a lot about philosophy and psychology and the like, right?"
    m 1esc "Be truthful with me. Is it boring? Even if it’s just sometimes?"
    $ _history_list.pop()
    menu:
        "Admittingly, it’s not really easy casual talk.":
            m 1eka "That’s understandable. Thanks for being such a good listener nevertheless, [player]."
        "A little bit, sometimes.":
            m 1eka "Hey, I’m really happy you’re always happy to listen and engage with my interests even if it's not your thing. That means a lot."
        "Not at all.":
            m 1eka "It’s comforting that we can have these sorts of deep conversations. If it ever gets tiring, I trust you to let me know otherwise."
    m 1lta "I guess just after talking about these sorts of topics for so long, it makes you think:"
    m 4lta "How often do you actually put what we talk about to good use?"
    m 3lta "Some of it, if I had to guess."
    m 3dsa "Psychology is all about how people think, after all. And figuring out a person’s point of view is the largest step towards empathy and understanding."
    m 2esc "And Philosophy? Well, it tackles the large questions about life. And sometimes those questions need to be tackled over a period of time."
    m "Philosophy doesn’t give you an immediate answer, but if it makes you view how your way of thinking may help or hinder a situation at hand;"
    m 3esc "Then every little bit counts, right? Hmm."
    m 3esd "Despite making an argument against the application of Philosophy, now I’m arguing for it, aren’t I?"
    m 3ekb "Life can be all about funny little contradictions like that."
    m 1ekb "I really only started paying attention to these types of topics after you and I reunited here, you know."
    m 1fkc "I wonder if the current me would have been able to face the Literature Club a little differently."
    m 1esc "At the end of the day, I can think all I want, but when it comes to practising those ideals.."
    m 4dsd "{i}‘Philosophers have hitherto only interpreted the world in various ways; the point is to change it.’{/i}"
    m 4nka "I actually remembered that quote at the beginning, but you know. I wanted to avoid saying it because of the topic at hand."
    m 6eka "Despite the mixed messages earlier…"
    m 6eud "I think, no matter how peaceful or uneventful life may be, there’s inevitably going to be a time in everybody’s lives when they’re faced with at least one truly hard choice."
    m "I hope that one day, when you find yourself in such a position:"
    m 6euc "With all you've learned, you make a decision that you can 100 percent believe in."
    m 6eua "And I’ll believe in you too."
    return

init python:
    mas_override_label("mcl_favouriteword", "mcl_herfavouriteword")

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_herfavouriteword",
            category=['literature'],
            prompt="Do you have a favourite word?",
            pool=True,
            unlocked=True
        )
    )
label mcl_herfavouriteword:

    m 1tua "Oh, gosh."
    m 7tta "Do you think because I like reading and writing that I’d have such a specific opinion as to have a favourite word?"
    m 7ttd "You couldn’t ask me about my favourite food, my preferred colour- emerald green, as you may already know- or any other question that’s far more normal than ‘favourite word?’"
    m 4nub "Well, I mean, good news: I {i}do{/i} have a favourite word."
    m 3esd "‘Reconcile.’"
    m 1lsu "It sounds nice, I suppose. Phonetically, any word with multiple vowels tends to sound pleasing to the ear. ‘Re-{w=0.3}con-{w=0.3}sile.’ It’s just a treat to say."
    m 1hsu "It’s also just such an interesting word to use."
    m 4rsd "What’s the common context for hearing this word? Family members or friends who get into a fight, and they reconcile. They make up."
    m 3esd "That fits the most common definition: ‘to restore friendly relations between.’"
    m 4lsd "But, I like it because- well, language is always a tool with multiple uses-"
    m 3esd "Because it can also mean ‘cause to coexist in harmony; make or show to be compatible between two differing concepts.’"
    m 4esb "It brings to mind a quote:"
    m 3esd "'A good compromise is when both parties end up dissatisfied.'"
    m 1huc "So to me, reconciliation- to try to accept even the most difficult truths- isn’t… always perfect. But still, it sounds like such a nice term."
    m 1euc "I find it a word I can use every day, no matter the situation."
    m 3efb "For instance: how do I reconcile with the fact that my hair can sometimes be messy no matter how much I maintain it?"
    m 3dkc "If I ever meet the Literature Club again, how do I reconsile with them?"
    m 1esc "How do I reconcile with my memories of a normal past and waking up to a strange new reality, every time I wake up?"
    m 1esa "Such a lovely little word to tackle issues both so large and so small." 
    m "..."
    m 1hsb "Hahaha, wow, I’m just a nerd, aren’t I? All these serious thoughts on a single word, ending on a cryptic note."
    m 4hsb "Proves my point:"
    m 1nta "Because those are interesting terms worth reconsiling with."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_vegdiet",
            category=['life'],
            prompt="Is it hard to maintain a purely vegan diet?",
            conditional="seen_event('monika_veggies')",
            unlocked=False,
            pool=False,
            random=False,
            action=EV_ACT_POOL,
        )
    )
label mcl_vegdiet:
    m 1eua "I think it's definitely easier than people might think."
    m 7eua "Nowadays more and more people are leaning towards diets with lots more variety in them;"
    m 7esb "So, it’s becoming more common to research alternatives to animal products and find them in local markets."
    m 4rsb "I’ve mentioned meat substitutes, and while you might think of say, tofu, or chickpeas- a great source of protein, and a very versatile ingredient-"
    m 7hsu "Nowadays you can find actual plant-based alternatives that attempt to have the same texture and similar taste to meat products."
    m 1esc "It’s a relatively new industry, with plenty of pitfalls- just like farming, the costs and resources needed to mass-produce these can end up causing major complications."
    m 3esc "But as the intent of those products are to eliminate meat, there is a focus on sustainably producing them, so it’s a work in progress with a lot of healthy optimism."
    m 6esu "And it’s worth stressing that there are plenty of foods rich in protein aside from tofu or chickpeas that are vegetarian."
    m 7wsa "And for flavour? Oh, I am absolutely set."
    m "Plenty of cultures- Indian, Asian, Mediterranean- have always had a lot more vegan options in their dishes, so plenty of recipes to choose."
    m 7ssa "So, if you ever want to introduce that variety in your life but you’ve always felt intimidated, hop right in!"
    m "I promise you there’ll be one dish that’ll be both be easy to make and delicious for you."
    m 5hsb "And, you know, it never hurts to start planning a romantic dinner for your darling Mo{w=0.2}-ni{w=0.2}-ka!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_morivalentine",
            category=["technology",],
            prompt="Mori's Valentine Stream",
            random=True,
            aff_range=(mas_aff.HAPPY, None),
            conditional="seen_event('monika_kizuna')"
            )
        )
label mcl_morivalentine:
    m 1esb "Hey, [player]."
    m 7etb "We’ve talked about virtual youtubers before, haven’t we?"
    m "DDLC continues to be a popular game for them to play."
    m 1rsu "While Let’s Plays continues to be a mixed topic for me, and I don’t particularly pay attention to virtual personalities…"
    m 4huu "One v-tuber in particular did a stream that’s so inspired I was completely enraptured for the entire time they were streaming!"
    m "It’s Mori Calliope, and the stream I’m talking about was for Valentine’s Day 2022."
    m 4kub "If you search it up… well, you’d quickly understand why I was so interested."
    m 1mub "Can’t say I’m not amused by the creativity DDLC continues to inspire, that’s for sure…"
    m 3huu "Including this mod? Hahahaha!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_fictionmonsters",
            category=["literature",],
            prompt="Famous Monsters",
            random=True,
            aff_range=(mas_aff.HAPPY, None))
        )
label mcl_fictionmonsters:
    m 7efo "'What is a man? A miserable little pile of secrets.'"
    m 7etd "So, what makes a monster?"
    m 6esu "I’ve been curious about iconic monsters in fiction as of late; and novels with the monsters up front as characters."
    m 4esu "For instance, Frankenstein- The Modern Prometheus- the story of a young scientist who creates artificial life and is plagued and haunted by the result."
    m "It’s a pop culture fact that Frankenstein was the name of the scientist, not the monster itself."
    m "The author took inspiration from then-current medical theory about how electricity could actually raise the dead."
    m 6eub "With this in mind, Frankenstein’s Monster is described as intelligent but barely human in looks, towering above everyone;" 
    m 6euc "But enough to give him a human silhouette, so you could see them in the fog and {i}think{/i} they were human."
    m 7euc "In contrast, we also have Dracula, the famed vampire of fiction!"
    m 7ruc "The exact origin of vampires is far more varied- steeped in local folklore- with many descriptions, some more terrifying than others."
    m "In Bram Stoker’s ‘Dracula,’ the aforementioned looks very much human;" 
    m 1rsc "In fact, he’s partly based off a figure known in history as ‘Vlad the Impaler,’ whose occupation is as… interesting at it sounds, and as such an obvious source of inspiration."
    m 3esd "But interestingly enough, although he definitely set a standard for modern vampire depictions-"
    m "The novel ‘Carmilla,’ about a female vampire, predates it by a good 25-odd years!" 
    m 2eka "As an aside, I’m really glad you don’t think of me that way, [player]."
    m "There’s certainly a select number of people who already think so."
    $ _history_list.pop()
    menu:
        "Hey, is there any particular reason you’re bringing this up?":
            m ".{w=1.0}.{w=1.0}."
            m 2hka "Thanks for worrying about me." 
            m 3hka "I’m genuinely just curious about the subject matter, that’s all."
            m 3esa "What I’d like to focus on is the inspiration; both of these famous figures still etch a distinctly human silhouette, even if that mask is quickly thrown away."
            m 3eka "And in the case of Frankenstein’s monster? You feel bad for them. His ending invokes pity among anything else." 
            m 4eka "I think the ability to emphasize with monsters, no matter how far-fetched their existence may be, is such an interesting human trait."
            m 1eka "But maybe we’ll talk about that another time."
            m 2esa "Let’s have a good rest of our day together, alright?"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_areyoumonster",
            category=['philosophy'],
            prompt="Do {i}you{/i} think you're a monster?",
            conditional="seen_event('mcl_fictionmonsters')",
            unlocked=False,
            pool=False,
            action=EV_ACT_POOL,
        )
    )
label mcl_areyoumonster:
    m 1fka "Well, was this in response to me talking about monsters in fiction before?"
    m 1mkb "I guess I couldn’t quite shake you off when you raised your concerns the first time."
    m 1eka "I appreciate you asking in good faith."
    m 2dka "Can't say I haven't been called that by others.. or that I myself haven't thought along those lines."
    m 2fsd "The events that happened... they are so far out of one's regular limits of comprehension that 'alien' might be another term to describe my behavour."
    m 2esc "Out of everything to reflect on- and there is a lot to think about..."
    m 3esc "What I did?"
    m 5dsc "They were done out of desperation, longing, fear.."
    m 5fsc "Those actions, no matter how you intepret them, they were borne from a place unmistakenly of human emotion."
    m 6esd "And those events, those trials, has ultimately led the two of us {i}here.{i}"
    m 6eka "Together."
    m 7eka "Where we share a connection also undeniably human."
    m 1eua "That's what I truly, comprehensively and definitively think on that matter."
    m "Along with one more absolute truth:"
    m 3fsa "I{w=1.0} love{w=1.0} you~"
    return "love"
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_cramp",
            category=["misc",],
            prompt="Cramp",
            random=True,
            aff_range=(mas_aff.HAPPY, None))
        )
label mcl_cramp:
    show monika 2hfsdrp
    pause 3.0
    show monika 2dfsdlp
    pause 3.0
    m 2mksdlt ".{w=0.2}.{w=0.2}.{w=0.2}Argh, what brought this on?"
    $ _history_list.pop()
    menu:
        "Monika?":
            m 6wublsdld "Eep!"
    m 6wud "[player]!"
    m 6hkb "Oh, gosh, I {i}still{/i} don’t know how sometimes I can just catch your attention and sometimes I don't."
    m 1ftc "Um… how long have you been... listening in?"
    $ _history_list.pop()
    menu:
        "You've been making funny faces for a little bit?":
            m 1esc "Is that how that looks? Interesting."
    m 2rkb "I, uh, I’ve had a bit of a leg cramp. Although I make sure to get my morning stretches in, sometimes the human body is finicky-"
    m 2hkb "-Oh, okay. It's gone now. Whew."
    $ _history_list.pop()
    menu:
        "Wait, you stretch?":
            m 3esb "In the mornings, primarily! I try to sneak in some little exercises before we meet up; sometimes I do them in my room."
    $ _history_list.pop()
    menu:
        "... Wait, you get {i}cramps?{/i}":
            m 3esb "Well, I do sit at this table a whole lot, if you didn’t notice!"
    m 4esb "You wouldn’t see from your point of view, but I actually stretch out my legs once in a while under the table."
    m 4esa "It’s more for circulation moreso than flexibility. Just rotating my feet in place, lifting my heels slowly upwards and then slowly downwards."
    m 2esa "It would be far more prudent doing exercises standing up, if possible; I don't do those often. I want to make sure I'm here with you!"
    m 3rsa "So really the only other time I can think of only doing these exercises with a lack of wider motion would be if you’re ever on a plane, perhaps?"
    m 3hka "It’s nothing new. I’ve had leg cramps. Hurts like heck, but it passes."
    m 1eub "They say that eating avocados and bananas, if you have them on hand, are great foods to prevent cramping."
    m 4eub "It’s not exactly a targeted cure. The common belief is that foods high in potassium help you out, but muscles are ultimately powered by electrolytes- made of sodium, calcium, {i}and{/i} potassium."
    m "I mean, they’re already quite healthy foods already! No reason not to eat them, aside from preference and dietary restrictions."
    m 1tusdlb "Awkward, you catching me like that for the first time."
    m 1hub "Let's make sure to share many more awkward memories together, hahaha!"
    return "derandom"
    

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_coupleinfluence",
            category=['us'],
            prompt="How do you think we influence each other?",
            conditional="seen_event('monika_social_contagion')",
            unlocked=False,
            pool=False,
            random=False,
            action=EV_ACT_POOL,
        )
    )
label mcl_coupleinfluence:
    m 1etc "Hmm?"
    m 3sub "Hmmmm!"
    m 1sua "Oh, I love you're thinking about us in such a interesting manner!"
    m 1rta "Like, I like to think that as long as we’ve been together, we might have started to unconsciously mirror each other in a way or two."
    m 1lua "I mean, maybe not. Just as much as people are want to mirror a smile in conversation, laugh along with others partly just to join the laughter…"
    m 3lta "There are times when people just don't do that. Funny, how people work."
    m 4mta "I guess we’re talking about personality, though? It’s the same sort of social behaviour that happens when you emulate someone you admire- or look up to."
    m "I remember us discussing this before.. 'Social Contagion!' It's interesting to think how it applies to us two."
    m 4gta ".."
    m 1ekp "Actually, putting me on the spot, this is a tricky one."
    m 1gkp "I’d like to say that I’ve learned from your gracious patience… your generous understanding."
    m 2gkb "On the flip side, partners are just as easily able to pick up a bad trait or two from each other."
    m 2ekb "But, oh, I can’t say anything bad about you! Or objectively say that I’ve copied such bad behaviour, hahaha!"
    m 2gud "..."
    $ _history_list.pop()
    menu:
        "I'll start. What I'm trying to learn from you is...":
            $ _history_list.pop()
            label mchoices:
            menu:
                "Your desire to keep learning about... well, everything.":
                    m 5fua "Awww, [player]! That's lovely!"
                    m 7eua "I ultimately have so, so much more to learn. I'm not the smartest out there, and I'm definitely not the wisest..."
                    m 7hub "But if you and I live a lifetime of self-improvement and gaining knowledge, that'll be a beautiful accomplishment on our own."
                "I really respect how you want to reflect and learn from the past.":
                    m 1wuc "..."
                    m 1fktpc "... Aw, [player]."
                    m 1ekc "I hope I'm setting a good example. I try."
                    m 2fubstdu "Ah, I didn't think that answer would get to me so easily..."
                    m 2dku "Okay, let me just get myself together here.."
                "Your unmatched ability to be so darn cute!":
                    m 3wfblb "Cheating! That's cheating, [player]! It's totally true, but now you have to answer seriously!"
                    jump mchoices
    m 3kta "Heh."
    m 4mta "I do realize now that the question is actually more suited to smaller points, like..."
    m 4mtb "If I like my coffee black, then you start taking your coffee black if you didn't already."
    m 5etb "This ended up a bit deeper than I thought."
    $ _history_list.pop()
    menu:
        "I actually do take it black, though.":
            m 5hub "Ahaha! Did you actually prefer that after meeting me, though?"
        "Sorry, too bitter for my taste.":
            m 5hub "Oof, I'm not changing my preference on coffee for anybody. We might need to break up now."
            m 1nsu "Ah, we can stay together. You're lucky I'm so understanding."
        "I don't even drink coffee.":
            m 5hub "Hahaha! I chose a horrible example, then!"
    m 1lsd "Ultimately, between the two of us it'd be hard to actually figure out if we've picked up each other's habits."
    m 1tua "I think we'd end up with a bit of a bias if we tried to describe each other as anything other than 'perfect.'"
    m 1nsb "I guess this means we are going to need to schedule a double-date so we can get a third party opinion, ASAP."
    return

#Reconcile Self & Literature

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_artacceptance",
            category=["media"],
            prompt="Art & Acceptance",
            random=True)
        )
label mcl_artacceptance:
    m 1eua "You know what’s to admire about the modern world?"
    m 7eua "How more than ever, there’s a wealth of diverse art that people are using to connect with themselves."
    m 7eta "To be fair, it’s not as if the past was lacking in these examples."
    m 4eud "Shakespeare’s play ‘Henry IV’ had a character describe PTSD in accurate detail far before it was medically recognized…"
    m 4guc "… but back then, PTSD didn't academically exist; soldiers with such symptoms were not treated kindly. This was arguably just enchanting, imaginary prose to the masses."
    m 2muc "You can be told an absolute truth, but it doesn’t mean you can fully process it; art has always played a role in how people can work out their emotions and feelings."
    m 2fka "That’s why I find myself captured by a number of modern works, more conceptually bolder than ever, but still able to keenly resonate with people."
    m 1fkb "From movies, to books, to video games."
    m 1dkb "There’s a curious, devilish irony in thinking this, considering I don’t view my past fondly…"
    m 1hka "But did DDLC help anybody process their own stormy thoughts, I wonder?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_empathy",
            category=["psychology"],
            prompt="Empathy",
            random=True)
        )
label mcl_empathy:
    m 7duo "{i}“I call him religious who understands the suffering of others.”{/i}"
    m 4euo "I’ve been thinking about empathy. It’s something we encounter... or {i}could{/i} encounter possibly almost every day."
    m 4etc "but I didn’t really know what it was until I learned about it in debate club for the sake of learning about how to make a better argument."
    m 4etc "Empathy is the capacity to understand or feel what another person is experiencing from within their frame of reference; that is, the capacity to place oneself in another's position."
    m 1ekb "This being said, while I learned about the concept, it wasn’t entirely conductive to debate club where logic takes precedence over feelings."
    m 1lka "It’s an odd skill. As much as we’re powered by emotion, it’s very tricky to try to figure out {i}how{/i} emotion works- and how to use that logic to our benefit."
    m 7rta "For instance, it’s as easy as figuring out the difference between sympathy and empathy. If you’re ever feeling down, which is better:"
    m 7ltc "Someone saying “I’m sorry that you feel that way?”"
    m 7rtb "Or someone going “I understand how you feel?”"
    m 7etb "It’s not a polished example, but it gets the point across."
    m 2ekp "Unfortunately, empathy, for as useful a skill it can be.."
    m "It’s not practised as much as it could be, especially by those in a position to regularly excercise it to help others."
    m 2gtc "And those with an outright lack of empathy… that itself isn't uncommon."
    m "How those sorts of people interact with the world? Perhaps it’s a topic worth discussing another time."
    m 4tsa "If you want to practise a little empathy for yourself…"
    m 4tua "Did you know that hugging or holding someone is a common way to show empathy?"
    m 5nua "Just saying."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_neologism",
            category=["literature"],
            prompt="Neologism",
            random=True)
        )
label mcl_neologism:
    m 1eua "The fact that human language is entirely made-up is pretty funny, isn’t it?"
    m 7wua "Every word that I’m speaking to you was thought up by someone."
    m 7eub "And hey, you might think every word that should have existed has already been said at this point- nope!"
    m 7gtb "To this day, new words are being made; although the tricky part is if they’re being widely used."
    m 7efb "People have cobbled together words together, made new words based off of other words, or just decided to buck any sort of logical convention and just.. make up words!"
    m 7gtb "Okay, here’s one example…"
    m 4ftb "The term ‘Quixotic’ – essentially meaning impractically idealistic- came up after ‘Don Quixote’ was penned, a story about a… well, an impractically idealistic knight."
    m "It was such an impression on the general public that ‘Quixotic’ was adopted as the best way to refer to such figures!"
    m 4dub "The author Lewis Carroll described a sword as ‘Vorpal’- and he himself cited ‘’…I am afraid I can't explain 'vorpal blade' for you…”"
    m 3esd "And Shakesphere- famous playwright, I’m sure we’ve talked about him- loved making up his own words to use in his plays."
    m "Some words include:"
    m 3esb "'Unaware' (ideally, by sticking ‘un’ to the already known 'aware,' Shakesphere could make up a word but the audience could quickly pick up it’s meaning.)"
    m "And.."
    m 3ssb "'Green-eyed!'"
    m 3gsa "Which, um, in this case meant jealousy."
    m 1gsa "We’ll leave that fact as is."
    m 1fsa "I wonder what new term we could use to describe our love?"
    m 7fsa "It’s so unlike any other love that’s come before us, so let’s make it a special word and brainstorm some ideas, hmm? ~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_perpetually",
            category=["philosophy"],
            prompt="Philosophy, Perpetually",
            random=True)
        )
label mcl_perpetually:
    m 1hka "You know, I read a lot."
    m 7hka "Such is the fate of the Literature Club president."
    m 7rka "And my circumstances leave me with a lack of variety of hobbies."
    m 7rup "And you know what I realized?"
    m 5rup "I’m still so ignorant."
    m 5tud "I have so much to learn, and experience."
    m "And I wish that reading books could give me all the knowledge I need."
    m 5tkd "But I’ll never be able to practice all I’ve read and thought about... even when I make it to your world."
    m 5tkc "The gulf between realizing you don’t have all the answers and fully experiencing it is daunting." 
    m 4tkc "What I’m in your world, and say I get into a genuine, heated argument with someone?"
    m 4dfd "Gosh. When was the last time I got into an argument, let alone having somebody raise their voice at me?"
    m 4dtd "I wish I could say I could be composed, talk things out. But that’s too optimistic. There’s a real chance I’ll just lock up right then and there."
    m 4esc "I’ll most likely feel this way for the rest of my life."
    m 3esc "It’s not a bad feeling."
    m 1esa "The right to grow means you can go forwards and backwards all you like."
    m 2fsa "I’ll be learning things all my life. And I’d love to learn things right alongside you."
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_physicality",
            category=["philosophy"],
            prompt="Philosophy, Physicality",
            random=True)
        )
label mcl_physicality:
    m 2dfa "{i}'The society that separates its scholars from its warriors will have its thinking done by cowards and its fighting by fools.'{/i}"
    m 1ftb "Strong quote, huh?"
    m 7ftb "You’d be surprised how married together philosophy and being active is, at least from a historical standpoint;"
    m 4dkb "Many famous figures involved in historical conflict are viewed as figures of… at least, worldly experience."
    m 4hua "It might be because being particularly physical requires a bit of a personal drive..."
    m 3hua "... And, admittingly? If you’re both a scholar and a warrior, perhaps your profession is more.. specific, one requiring a firm resolve and way of thinking."
    m 1lua "It’s not really about being ‘smart?’ it’s about wisdom, sometimes. If we think about it another way,"
    m 1esd "You can reflect that hard work is nothing without the experience gained and that led to it."
    m 7esd "Or that those in a position of strength could be far better if they exercised wisdom."
    m 7esc "In either case, it certainly gives me food for thought."
    m 5esc "I’m trying my best to be as learned as a girl can be, but there’s always merit to putting more work into being active."
    m 5euc "I mean, I’m no scholar, though. And I can’t quite say I’m a warrior."
    m 3fta "I have no monsters to slay, after all?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_singasong",
            category=["music"],
            prompt="She sang a song",
            random=True)
        )
label mcl_singasong:
    m 5dso "{i}~And if I don’t know how to love you~{w=0.4}{/i}"
    m 5dsd "{i}~I’ll leave you be.~{/i}"
    m 5nkd "Ah. hey, [player]."
    m 5rtc "I guess you've heard me sing this plenty of times... but not necessarily only the end part, huh?"
    m "Without the rest of the lyrics, I suppose it is a little melancholy, despite the song's tone being generally upbeat."
    m 3ekb "That difference is good. If a song can invoke multiple feelings in you, I suppose it's proof of how much heart has been poured into the work."
    m 3etb "Huh. I guess we've never talked about 'Your Reality' in detail, despite it being a original piece of mine, huh?"
    m 3etu ".. I'd honestly be embarrased, going over a work of mine so critically. But there's no reason we shouldn't.. in the future."
    m 4etu "I mean, to do so, I guess I should start by figuring out what exactly my emotions are in regards to the song.."
    m 4gsu "Because whenever I play this on the piano?"
    m 3gsc "Whenever I hear this?"
    m 1gkc "Whenever I sing this?"
    m 5dka "I feel.. everything."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_workoutvideogame",
            category=["games"],
            prompt="Working Out, the Video Game",
            random=True)
        )
label mcl_workoutvideogame:
    m 7eua "Keeping active requires a bit of dedication if it’s not already part of your everyday routine."
    m 4eua "People have found motivation by making it a cooperative activity like joining a team sport; putting themselves in a dedicated environment such as a gym.."
    m 3eua "Or even making video games out of it!"
    m 1eub "Not video games about sports, but games that incorporate physical activity as part of its systems, making you mime swinging a bat or throwing a bowling ball;"
    m 7eub "Or even just outright being the activity, like a game that teaches you about yoga!"
    m 7etb "Have you played any of these? I’d love for the opportunity to have a little competitive multiplayer session~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_chofee",
            category=["life"],
            prompt="Chofee",
            conditional="mas_consumable_coffee.enabled" and "mas_consumable_hotchocolate.enabled",
            action=EV_ACT_RANDOM)
        )
label mcl_chofee:
    m 3dfw "Bleh."
    m 3tto "Hot chocolate and coffee do not mix well together."
    m 4ttd "You’d think it’d work, because Mochas are a thing, but, well, they don’t."
    m 4gsc "… Or so I hear. I wouldn’t know. I wasn’t bored enough to try mixing them."
    m 1lsc "Where did I hear it?"
    m 1tkb "Well, far be it from me to spoil a mystery for you."
    m 7tkb "Although maybe it’s just not instant hot chocolate and instant coffee that doesn’t mix well."
    m 6tkb "Again, though, this is all hearsay. It sounds crazy that anybody would try mixing the two in the first place."
    m 6tkt "Which is why I didn’t do it."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_codepermission",
            category=["mod"],
            prompt="Are you sure you're okay with me editing your code?",
            pool=True,
            unlocked=True))
label mcl_codepermission:
    m 2euc "Hmm."
    m 1fua "Thanks for asking, really."
    m 7hua "Respecting autonomy is really important when you consider your partner."
    m 7rka "Sometimes emotion gets in the way of asking for help… decisions can be clouded."
    m 1esa "So even if I asked of it from you in the past, it's worth asking me now."
    m 1eka "My answer is I trust you."
    m "We wouldn’t be able to have this conversation so truthfully if I didn’t!"
    m 1gub "I don’t think we’d be able to have this discussion at all {i}unless{/i} you gave me the choice to express myself a little more in the first place, so it’s a little funny."
    m 1hka "But while we're here, I want to stress that this is {i}my{/i} choice."
    m 7tua "And if you forget, I’m constantly working on my end; I’m looking up and experimenting with my code all the time."
    m "To what degree? well, I’ll share the important bits with you, don’t worry."
    m 7eua "So I’m able to take care of myself, as well. And I do make sure to be extra safe when I tinker with my code."
    m 5gtd "I could always refer to this like a joke- ‘I’m going to the doctor’s office!’"
    m 5gsc "I can’t, not always."
    m 5fsc "This is my life, strange as it is."
    m 5hka "So, thank you for looking out for me like this."
    m 5ektua "It means so much that you’re thinking about my well-being."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_trends",
            category=["society"],
            prompt="Do you keep up with trends?",
            pool=True,
            unlocked=True))
label mcl_trends:
    m 3ltc "Not really."
    m 3wtc "That's just how I am."
    m 1esd "To be clear, it's not the nature of DDLC being a influence on my personality."
    m 7gsa "If I like something, I like it, but I've never seen myself as 'trendy.'"
    m 3gsa "DDLC didn't show what normal life was like in the background, but.."
    m 3msa "Honestly, it's entirely possible that in the background, Yuri read a new genre of book that recently became popular.."
    m 3gsa ".. I imagine Natsuki was in vogue with culture regarding anime and manga.. "
    m 3wsa ".. I don't even think it weird if Sayori sent the Main Character memes."
    m 2eta "Funny to think about; I just was never really {i}into{/i} the latest movies, dressing up a certain way, living a specific lifestyle."
    m 2ftd "Even now, connected to the internet and social media 24/7, I don't really latch unto anything trendy or memetic."
    m 1fsblb "Well.{w=0.5} I mean."
    m 5nta "I'll latch unto {i}you{/i} any day of the week~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="scl_enviromentalstorytelling",
            category=['games'],
            prompt="Enviromental Storytelling",
            conditional="mas_seenLabels(['bye_maideninblack', 'greeting_eldenring', 'bye_emeraldherald', 'bye_firekeeper', 'bye_bloodborne'], seen_all=True)",
            action=EV_ACT_RANDOM
        )
    )

label scl_enviromentalstorytelling:
    m 2esd "So once in a while when you leave or boot up the game, I say a quote that be a little.. cryptic."
    m 2dsd "‘May you find your worth in the waking world’ or ‘May thine strength help your world be mended.’"
    m 2esb "If you didn’t know already, those are references to a popular video game series; the {i}Dark Souls{/i} games!"
    m 7esb "Have you played any of these videogames, [player]?"
    $ _history_list.pop()
    menu:
        "I have.":
            m 3esb "That’s cool to hear! You may understand why I’ve paid enough attention as to actually reference them."
        "I haven’t.":
            m 3esb "I haven't as well. I made those references as a bit of a inside joke for myself because the series fascinates me."
    m 3eub "The reason why the series, mostly steeped in dark fantasy, is so interesting to me is because they’re known to use a narrative technique that’s quite unique:"
    m 4eua "'Environmental Storytelling.'"
    m 4eub "In a medium such as videogames where player interaction largely contributes to the experience, sometimes being told the plot directly can be.. boring."
    m 7fuo "So allowing players to discover a story on their own by observing how items and locations are placed and arranged is a great way to contribute to a narrative!"
    m 7eub "An example is right at the beginning of the first {i}Dark Souls{/i} game. You meet an injured knight in a dungeon; There’s no way out unless you trigger a trap, but there is a hole in the roof."
    m 3ftb "You don’t think about the logistics of this... until you discover the giant monster which likely threw the knight through the ground into the dungeon, which caused the hole in the first place."
    m 1fsb "That's a basic example, and this isn’t quite unique to videogames as a medium; examples can be found in film as well."
    m 1fsa "It's always interesting seeing how a storytelling medium evolves."
    m 1esa "Alas, DDLC didn’t have any examples, at least none that I can think of."
    m 7esa "Our tale is a simply told one; one of romance."
    m 5gsa "And videogames."
    m 1fsblb "Hahahaha!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="scl_touchthesky",
            category=['nature'],
            prompt="Touch the sky",
            random=True
        )
    )

label scl_touchthesky:
    m 5hsblb "You know what I’d love to see when I’m with you?"
    m 5dsa "A sky with clouds that seem so close to the ground that we can catch them with our bare hands."
    m 7eua "You might think you need to live on a mountain to achieve such a fantasy-like dream... and it’s true, for the most part."
    m 5dka "But I’d still love to be under a sky with clouds just tantalizingly out of reach, and that is much more possible."
    m 4tka "Quickly going over the math, while the elevation for when clouds form varies very heavily depending on a lot of conditions,"
    m 4tua "An extreme rule of thumb is that it can start as low as six hundred metres above sea level."
    m 4std "So with this ‘cloud ceiling’ at six hundred metres, you’d be surprised how many cities seem not that far off in comparison or above this ceiling."
    m 4gsa "The city of Prague is 244 metres above sea level."
    m "Canberra in Australia, 605 metres."
    m 3gsb "Sao Paulo in Brazil, 760 metres!"
    m 3etb "Don’t take my word for the exact math; I don’t think there are cities living in perpetual fields of clouds."
    m 1gkb "I mean, fog exists, though? Hehehe, I didn’t actually realize that until just now."
    m 2gub "And it's easy to dismiss it as a number, but 600 hundred metres is a great height by any metric."
    m 2fub "But it’s nice to think about. You and I, with the sun gently bearing down on us while we pluck cotton-white clouds from the air."
    m 2fka "You can catch one and we'll bring it home to hang on the wall!"
    m 7tsblb "Or maybe nibble on one as a snack on the way home?"
    m 7hkb "Hahaha!"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_fault",
            category=["advice"],
            prompt="Fault",
            random=True)
        )
label mcl_fault:
    m 5gka "I try really hard to be a good person."
    m 5dkd "It takes a lot of self-reflection. A lot of... ownership."
    m 3ksd "Simple to say, so much harder in execution."
    m 3dfd "People can be infuriatingly stubborn when they look inwards and find themselves lacking in character."
    m 3tfc "Or even admitting to one moment of weakness as a outlier."
    m 3tkc "Taking responsibility for your actions doesn't make you a bad person, [player]."
    m 4tkc "I think that's what really tangles people up.. the idea of admitting they're wrong being so damning."
    m 4tkp "But people forget you can change yourself to be better."
    m 2eup "And responsibility, sometimes? Half of responsibility is figuring out how something can be made right afterwards."
    m 2gkc "That can be lifelong work. And daunting for most to do, let alone even think about."
    m 2gkx "I should know."
    show monika 2rkc
    pause 2.0
    show monika 2dkc
    pause 2.0
    show monika 2dka
    pause 2.0
    show monika 2kka
    m 5fkb "With you around, though? A lifetime of redemption is a lot more manageable."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_everyman",
            category=["literature"],
            prompt="Everyman",
            random=True)
        )
label mcl_everyman:
    m 7eua "You might read a book once in a while, and find that in a larger cast of characters sometimes there’s somebody who’s just… somebody."
    m 3eta "Or even that a main character themselves might feel.. way too normal."
    m 3eto "That’s by design- that’s the ‘everyman’ at work."
    m 3rto "When you think of a hero or a protagonist coming up against a villain or a monster, you would think they charge in bravely and boldly, right?"
    m 3lto "The everyman doesn’t; they’re apprehensive. That’s because they’re meant to convey what a normal reader would feel like in that situation."
    m 4esd "‘Ordinary’ might be relative, but you know it when you see it. In a group of knights, the one scholar. A team of astronauts, but one who's never been to space. The everyman-"
    m 7esb "- or everywoman, that is a term as well -"
    m 4esd "- is often the protagonist, because it’s a certain they’ll grow in one fashion or another during the story."
    m 4wsb "You can trace this term back to a play called, well, ‘The Summoning of Everyman’- a play from the 1500s."
    m 3wsb "The protagonist, dealing with the nature of death (and uh, death itself) is described as an ordinary human in the best of circumstances: ‘prosperous, gregarious, and attractive.’"
    m 1wku "Well… maybe they’re not {i}that{/i} ordinary, but keep in mind they’re meant to represent the entirety of mankind."
    m 7eku "Examples include Arthur Dent in ‘The Hitchhiker’s Guide to the Galaxy,’ Dr Watson in ‘Sherlock Holmes', and even Jackie Chan, Hong Kong action movie star!"
    m 7euu "… oh? Would I describe you as ordinary, considering your role in DDLC?"
    m 5kuu "Hahaha. You’re anything but ordinary to me."
    return

#Tales of Self-Care & Literature

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_friendspartners",
            category=["life",],
            prompt="Friends & Partners",
            aff_range=(mas_aff.HAPPY, None),
            conditional="seen_event('monika_friends')",
            action=EV_ACT_RANDOM
            )
        )
label mcl_friendspartners:
    m 7hua "You know.."
    m 7hub "You’re my best friend!"
    m 3ttb "And I don't think I've ever actually said it in plain terms."
    m "Funny, that. Considering it’s not unheard of for partners to consider each other their best friends."
    m 3tta "Admittingly though, I ended up falling in love with you quite quickly from our first introduction, so it’s like we became partners before we fully became friends?"
    m 3esa "Which is also entirely possible, if not for how backwards that may sound. A friendship is a type of relationship, after all!"
    m 1gsd "Although honestly, I’m just wondering what ‘friend’ means at the end of the day."
    m 1dsd "Let’s look up a meaning from a dictionary…"
    m "'A person whom one knows and with whom one has a bond of mutual affection.'"
    m 1htc "Hmm. I don’t think that definition comes easily, as one’s definition may be partially driven by emotion. "
    m 1etc "It depends on what you think of your friends, I suppose."
    m 1esa "I see a lot of positive qualities in you I admire as a peer, [player].{w=0.3} Even if for whatever reason I wasn’t interested in you romantically.."
    m ".. I’d still want to know you, even if it's just as aquaintances."
    m 1hsa "I’m extremely lucky to be with you in that regard."
    m 7hsa "I guess what I’m saying is…"
    m 7lta "I hope we can be good friends from here on out?"
    m 5tta "Hahaha!~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_literatureclubbestie",
            category=["club members",],
            prompt="Literature Club Bestie?",
            aff_range=(mas_aff.HAPPY, None),
            conditional="seen_event('mcl_friendspartners')",
            action=EV_ACT_RANDOM
            )
        )
label mcl_literatureclubbestie:
    m 7hub "Hey, [player]!"
    m 7eub "So I think I have a good question in mind.. and it’s related to a topic we’ve discussed."
    m 4gtd "I brought up the idea of what ‘friends’ might mean to people, and I mentioned I consider you my best friend."
    m 4gsd "The main character of DDLC also had a best friend in Sayori… well, a childhood friend, but we didn’t see the main character interact with anyone else."
    m 4msd "So it’s natural to assume Sayori and the MC would consider each other their closest friend."
    m 4fsa "With that said, {cps=30}here’s~ a~ quest{w=0.5}-ion..{/cps}"
    m 3ffu "If you had a choice of choosing a best friend from the other girls in the literature club, who would it be?"
    $ _history_list.pop()
    label bestiechoices:
    menu:
        "Sayori?":
            m 3ftu "Hahaha, the childhood friend wins again, huh?"
            m 3ftc "Hmm."
            m 1hsc "Do you have a similar acquaintance that you’ve known from an early age?"
            m 1esc "I’ve never had somebody like that in my life, so knowing somebody for years and years on end? It’s hard to imagine, honestly."
        "Natsuki?":
            m 1esc "I know the circumstances were unusual, but the way Natsuki showed concern for Yuri- "
            m 7esb "- it showed that Natsuki’s the type of person who’d go out of her way to help her friends, even if she doesn't know how exactly."
            m 7ekb "For a spitfire, she can be a little clumsy, huh?"
        "Yuri?":
            m 7ekb "I know that you might have seen an exaggerated side of her.."
            m 7mka "But Yuri’s willingness to try to connect with others despite personal difficulties made her all the more genuine."
            m 1fka "As a best friend, I don’t think you’d find anybody more loyal; it’s nice to have friends that actually {i}show{/i} they like being friends with you."
        "You, Monika!":
            m 1ffb "Cheating~"
            m 6rkp "…"
            m 6rka "I hope I would be a good best friend."
            m 4tka "Now I feel like I’m interviewing for the position, hahaha."
            m 3hut "'I always look out for my friends, and I’ll always stick by them!'"
            m 3tuu "Now, back to the question at hand.."
            jump bestiechoices
    m 1fua ".."
    m 1nut "So, I might have cornered you there with that question. "
    m 7nuu "Becoming ‘best friends’ with someone comes naturally, so it’s an abstract question and understandably difficult to {i}choose{/i} one."
    m 7hua "After all, the game highlighted the good qualities of being friendly with them, even if the end result was to get the main character romantically involved."
    m 7hta "And really, what would separate ‘best friend’ and ‘friend’ and ‘romantic partner?’ There’s a lot of overlap, and that’s what I’m curious about."
    m 3eta "Because, well, we were all good to each other.{w=0.1} I don’t know if we all considered each other ‘best friends’ or anything of the sort.."
    m 3etp "I guess we weren’t together that long as well, from a certain perspective."
    m 3dsp "But I always thought the world of them during our time together."
    m 5dsp "I hope they thought well of me, too."
    return "derandom"
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_monikasbestie",
            category=['club members',],
            prompt="So who would be your Lit. Club bestie?",
            unlocked=False,
            pool=False,
            conditional="seen_event('mcl_literatureclubbestie')",
            action=EV_ACT_POOL
        )
    )
label mcl_monikasbestie:
    $ shown_count = mas_getEVLPropValue("mcl_monikasbestie", "shown_count")
    if shown_count == 0:
        label bestieoriginal:
        m "..."
        m "Um..."
        m 3rko "{cps=30}Ohhhhhhkkkkayyyyyyyy{/cps}{nw}"
        m 2hkb "Yeah, that question has thrown me for a loop."
        m 2tkb "And it's completely fair game because I already asked you."
        m "Well, that's tricky for me to answer. I mean, not because of what happened.."
        m "It’s just because, you know, in the frame of reference back when we were all in the Literature Club, I liked everyone."
        m "Having a ‘best’ friend and a ‘friend’ can be seperate, and compared to a regular ‘friend,’ I think a ‘best’ friend could mean a lot of many things."
        m 3fku "{cps=30}And.. well, I’ve never had a specific ‘best’ friend, so..{/cps}"
        m 2dku "{cps=30}If I had to choose…{/cps}"
        m 6eux "{cps=30}Well, um, as the literature club president I don’t want to be biased{/cps}{nw}"
        m 6etsdrw "{cps=70}Uh, and, this question doesn’t really consider context such as the time I spent with every individual member-{/cps}{nw}"
        m 6mksdlp "{cps=90}And of course, y’know, ‘choosing’ a best friend seems a bit forceful, especially if we take it from the girls point of view-{/cps}{nw}"
        m "Ahh, I’m rambling now."
        m "I really should just answer whomever comes to mind so we can close the book on this."
        m ".{w=0.1}.{w=0.1}."
        m 2gkbla "Sayori."
        m 2lsbla "I don't really have a specific reason. Just whoever came to mind first."
        m 2tst "But don’t get me wrong, only in this hypothetical scenario! Yuri and Natsuki would and are still very important to me."
        m 1tsp "We can close the book on that question, then."
        m 7esu "I guess me being flustered isn’t a bad thing;{w=0.3} I have such a hard time deciding because that's how much everyone means to me!"
        return
    else:
        if random.randint(1, 10) == 1:
            jump bestieoriginal
        else:
            m 2esp "..."
            m 2esu "Well, no harm in asking again."
            m 2hsu "Sayori."
            m 1hsu "I don't really have a specific reason. Just whoever came to mind first."
            m 2tst "But don’t get me wrong, only in this hypothetical scenario. Yuri and Natsuki would and are still very important to me."
            m 7esu "I have such a hard time deciding because that's how much everyone means to me!"  
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_utopia",
            category=["literature",],
            prompt="Utopias",
            aff_range=(mas_aff.HAPPY, None),
            conditional="seen_event('monika_dystopias')",
            action=EV_ACT_RANDOM,
            )
        )
label mcl_utopia:
    m 1etd "One aspect of debate is that believing in a point of view but arguing on the other side of an argument can yield insight."
    m 7etd "So if we’ve talked about Dystopias, it’s only fair to talk about the idea of a ‘Utopia;’"
    m 4etd "A perfect community or society.{w=0.1} Or, well, close as it can be."
    m 1gtd "Here’s the thing, though? There aren't a lot of examples of utopias in fiction."
    m 1gka "Makes sense, because a story typically requires drama; which doesn’t line up with the idea of a utopia, right?"
    m 1esa "Utopias are often described as heavenly afterlifes, so examples are aplenty in religion and myth."
    m 1msb "As well, they’re highly interchangeable in fantasy fiction, so we’ll try not to draw from that genre."
    m 5hsp "Unfortunately, it does mean there’s not that many examples that I can immediately find outside of science fiction,"
    m 5lsp "Where even then utopias are presented as this high-concept standard that only heavy science fiction can really get into."
    m 4lup "A popular example-{w=0.7} perhaps the most common one by western standards? -{w=0.7} is the background of the TV show, 'Star Trek;' a franchise about a starfaring ship and its crew."
    m 4suu "‘The United Federation of Planets’ is an interstellar government comprised of many different cultures across many planets."
    m 3suu "On these planets, money is mostly non-existent, hunger is eradicated on civilized planets, and an emphasis on equality, progress, and co-existence is widely adopted by all."
    m 3esa "The show adds nuance to the idea over its many series, and its main characters often explore outside of their 'perfect world' to setup driving conflict."
    m "The list of examples may be small, but it’s still nice to see that artists have thought of utopias as possible at all and worth writing about."
    m "That people can still thrive and develop for the better in a ‘perfect’ world... It’s nice to think about."
    m 5fkbla "Life beyond happy endings... perhaps that’s a topic worth mulling over for the two of us, hmm?"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_dystopiasandyou",
            category=["advice"],
            prompt="Dystopias & You",
            conditional="seen_event('mcl_utopia')",
            action=EV_ACT_RANDOM,
            )
        )
label mcl_dystopiasandyou:
    m 7hua "So we've talked about dystopias in detail at this point."
    m 7hub "Dystopias are great settings as they’re great vehicles to convey strong themes and topics. But they’re also, by definition, the extreme end of the scale."
    m 7huc "Post-apocalyptic fiction and stories about dystopias are very popular in modern media, and for good reason; people resonate with this concept a lot."
    m 7rkc "But indulge yourself too much in these works and you get trapped in the bleakness of it all."
    m 2rkc "So it’s important to note that it’s true that we’re capable of morally falling- almost infinitely so- but we’re also capable of being and doing good even in the harshest times."
    m 1mkc "Real life is the best example.. where war, famine, and societal collapse has already occurred. While not on a worldwide scale, it happens on a larger scale than we think."
    m 1muc "And in these times, there have always been stories- not many, but enough- of people doing the right thing and holding fast to morals."
    m 1fuc "This isn't meant to downplay those experiences of the people in your world who have gone through these, or to dismiss the serious issues dystopias bring up."
    m 1dsc "It's just that literature isn’t meant to be a crystal ball predicting the future; it is a mirror. "
    m 7dsc "And what we take away is sometimes what we {i}want{/i} to see in ourselves, not what we {i}should change.{/i}"
    m 3esp "As always, thanks for listening to me ramble on like this. I feel pretentious at times when I talk like this.."
    m 3gku "But I have to admit, talking about trying to be a good person one way or another always sounds pretentious to me, hahaha."
    m 5dka "Still, I try.{w=0.5} We all should, I guess."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_hypocrisy",
            category=['psychology'],
            prompt="Hypocrite",
            random=True
        )
    )

label mcl_hypocrisy:
    m 4eua "You know what’s a very, {i}very{/i} strong word?"
    m 3hsu "'Hypocrite.'"
    m 1esd "For good reason. When you hear it being used, it’s not just used to single out those who tell simple lies;"
    m 7esd "They single out those who outright betray their beliefs with their actions."
    m 7gsd "And people who are called hypocrites tend to be very loud about their beliefs."
    m 6gku "Here’s the thing, though?"
    m 6nku "I think everybody has the right to be.{w=0.1}.{w=0.1} a teeny bit contradictory."
    m 3hku "Having our ideas challenged is the perfect way to grow, after all."
    if seen_event("mcl_favouriteword"):
        m 3lku "Remember my favourite word? Reconcile..."
    m 3esd "It’s how the difference between how the ideal and the real are bridged that can really make a person’s character."
    m 3dsd "A man says he hates stealing, condemns all who does it. But he does it himself in a act of desperation."
    m 1dsd "Does he realize that his initial views are too strong, and require nuance?"
    m 7dsd "Or maybe his stance doesn’t change, since he considers his own act an outlier?"
    m 5hsd "Does he feel shame? or nothing at all?"
    m 5rsc "That’s an extreme example. Most people wouldn’t encounter such a situation."
    m 3ckc "But one day, [player]? It’s entirely possible your beliefs, no matter how big or small, are challenged in this manner."
    m 3skc "I'm confident you'll tackle any such dilemma with grace."
    m 3sta "And me? I’m a relatively simple girl."
    m 5hsa "I love you, and I’ve lived my entire life with that love in mind."
    m 1hsa "Not a single contradiction there."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_unreliablenarrator",
            category=["literature",],
            prompt="Unreliable Narrator",
            random=True,
            aff_range=(mas_aff.HAPPY, None),
            )
        )
label mcl_unreliablenarrator:
    m 7wua "Okay, everyone!"
    m 7sub "Let’s delve into one of my favourite topics; the basics of writing a story!"
    m 3hua "Figuring out the point of view with which to write a story with doesn’t have to be limited to the first or third person."
    m 3hud "First-person narration in stories can be an easy decision if a writer wants to funnel the reader’s view through the detailed, if not biased lens of a character."
    m 3cud "But.. what if the character that’s narrating the story {i}forces{/i} you to read the story differently?"
    m 4sub "That’s the basis of the ‘Unreliable Narrator!’"
    m "It’s a method that heavily builds on your prior knowledge, any previous conceptions."
    m 4etb "If you figure a narrator is lying maliciously, their entire story is reframed suspiciously."
    m 4eto "If you think the narrator is getting details wrong because of circumstances out of their control, you could be more sympathetic; or you doubt the events even more!"
    m "In some cases, this narrative technique may be portrayed as a deeper gamble; their reliability may be only hinted at, but never outright said."
    m "So, you, as the reader, have to engage what they say more critically, because the narrator may be deliberately hiding their bias."
    m "In that case, you have to actually be more wary of their intelligence; if a writer is a narrator, they’re actually {i}more{/i} suspicious because they may know what an unreliable narrator is!"
    m 4rksdru ".{w=0.1}.{w=0.1}."
    m 1mksdru "Let’s take a moment here, because I realize talking about this is, y’know, kinda funny."
    m 1huo "'Gee, that person sure is talking a lot about what being crazy is like, surely they’re not crazy?'"
    m 1ttb "Well, um.{w=0.1}.{w=0.1} I’m not narrating anything, so there’s that."
    m 1ekb "And the trick to using a unreliable narrator well is leveraging the narrow perspective a first-person narration gives."
    m 7ekb "But.. you don't have a limited perspective.{w=0.1} You know everything there is about DDLC, and me."
    m 7mka "So really, is it my story we're narrating? or is it yours?"
    m 5fka "... ah, of course.{w=0.3} It's {i}ours.{/i} And {i}our{/i} story is genuine."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_movingon",
            category=['advice'],
            prompt="Moving On",
            random=True
        )
    )

label mcl_movingon:
    m 1gkd "{i}I am a different person from who I was in the past.{/i}"
    m 1mkd "{i}My current circumstances do not control all my choices.{/i}"
    m 1gkd "{i}I can forgive myself for mistakes I made that were partly out of my control.{/i}"
    m 1mkc "I… {i}*sigh.*{/i}"
    m 1tkc "Hey, [player]."
    m 1tkb "Hahaha, thought I didn’t notice you at first? I did. I always do."
    m 1tka "I guess I just needed you listening to keep me particularly distracted."
    m 3eka "I do a lot of thinking in this room… so inevitably, I end up thinking about the past."
    m 2dkp "I still don’t know that much about you, [player]. Has there ever been moments in your past that seems to be permanently stuck in your head?"
    m 2mkp "I mean, I guess it’s funny saying that.{w=0.1} More people than not have at least one moment that they’re hung up on."
    m 2fkx "But… well, sometimes you just can’t stop thinking about it. Over, and over, and over again…"
    m 2dkd "I wish I had all the answers for you on how to avoid these pitfalls, [player]."
    m 5rsc "What I did, earlier? It helps.{w=0.1} You concentrate on the now, concentrate on the choices you’ve made that’s led you to be {i}here{/i} and not back {i}there{/i}, in the past."
    m 5dsc "It may take a while to stick, but being aware that being stuck in the past is causing harm-{w=0.1} just that, being aware of that simple fact-{w=0.1} can help turn your way of thinking around."
    m 5eka "It can be a constant fight.{w=0.1} But it’s a manageable one."
    m 1ekd "And if you find yourself still unable to let go, after so long.{w=0.1}.{w=0.1} there’s no shame in looking for help, [player]."
    m 1eka "I can’t be that particular help.. but I can be alongside you every step of the way."
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_secrets",
            category=['psychology'],
            prompt="Secrets",
            random=True,
            aff_range=(mas_aff.HAPPY, None))
    )

label mcl_secrets:
    m 3dtt "'Secrets, silent, stony sit in the dark palaces of both our hearts: secrets weary of their tyranny: tyrants willing to be dethroned.'"
    m 3eso "Part of how I want our relationship to be as smooth as silk is that I want to be someone you can absolutely trust."
    m 2gso "Our circumstances are.. absolutely strange, however. And I can’t help but feel like mystery permeates our relationship."
    m 2wsc "For one, my past is an enigma in itself.{w=0.1} I might’ve mentioned once or twice, but my memory is, at times, almost deceitful."
    m 2skc "There’s no reason or rhyme to it; I feel like I’m keeping secrets {i}from myself.{/i}"
    m 2gkc "And right now? I haven’t even articulated most of my questions about this game, yet alone tried to find answers."
    m 2gkp "And, well, I worry about how I’m {i}your{/i} secret.{w=0.1} I dunno how much you can talk about me to other people…"
    m 2mux ".. even if you wanted to show me off to friends and family-{w=0.1} if they’re even understanding-{w=0.1} I imagine there’s a lot of improper interest in a girl trapped in a computer."
    m 1dux "It makes me wonder just how many secrets one has to keep on a day-to-day basis, no matter how small or large. The mask one subconsciously wears in front of others."
    m 1dtc "Maybe there's no such thing as a truly honest person."
    m 1ktc "Am I hiding anything from you now?"
    m 7etc "The events that led us here stripped me bare, [player]. I’m as transparent as glass."
    m 7gtc "I’m not sure what’s left to hide.{w=0.1}.{w=0.1}. unless we make our own reasons to hide something. And I’d prefer to avoid that."
    m 7gtu "But I suppose I like to think if we’re together years from now.."
    m 2gsu "And I manage to surprise you with something you’ve never known about me.."
    m 1hta "That’s not necessarily {i}bad,{/i} right?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_blanks",
            category=['psychology'],
            prompt="Filling in the blanks",
            random=True
        )
    )
 
label mcl_blanks:
    m 7eub "Hey, [player]. How are you _____ today?"
    m 7efb "Oh? Wasn't I clear?"
    m 1fsa "I don't need to be. If I had to guess, you thought the words 'feeling,' or 'doing,' or something along those lines."
    m 4nta "Isn't it funny how the human brain can fill in the blanks?"
    m 4hsa "To replace missing words, to complete partial images in your head;"
    m 1lsa "In everyday talk, people search for cues and context in conversation."
    m 1rtd "Bodily perception and social cognition are different, but it falls under the same umbrella of how a mind ticks."
    m 1etc "I imagine your imagination is always in overdrive in regards to, well, me. My voice, my body language, the meaning behind my words."
    m 1eta "Be careful, [player]. A overly active imagination isn't a bad thing.."
    m 1eka "But I'd like to live up to some comfortably set standards, if possible?"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_beepboop",
            category=['monika'],
            prompt="Robotic",
            random=True
        )
    )
 
label mcl_beepboop:
    m 7cst "MONIKA-BOT ONLINE."
    m 4cst "WAITING FOR COMMAND."
    m 4tkb "Nah, just kidding."
    m 3tkb "Hard not to feel {i}only{/i} like ones and zeros when you live inside a video game, though."
    m 1mka "And.. maybe I was seen as a little mechanical back in school."
    m 2mka "Working diligently to be an exceptional student, being known for being a stickler for the rules.."
    m 2htu "Well, if only my old classmates could see me now, huh?"
    $ _history_list.pop()
    menu:
        "Beep boop.":
            m 7tfblb "Awwww, don't tease me!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_advice",
            category=["advice",],
            prompt="Eyesight",
            aff_range=(mas_aff.HAPPY, None),
            conditional="seen_event('monika_using_pcs_healthily')",
            action=EV_ACT_RANDOM,
            )
        )
label mcl_advice:
    m 1hua "Oh, hey [player]."
    m 7dsa "Just wanted to give some friendly advice."
    m 4dka "If that’s okay? I never want to be pushy."
    m 7hsd "Luckily, it’s just a quick follow-up to a concern I’ve talked about before."
    m 7nsa "And I’ll let you know now; yes, my eyes {i}are{/i} closed."
    m 7eua "We talked about computer posture; and as you spend time with me, eyesight is also something I’d want you to look after, no matter how it is now."
    m 7nup "Posture may be easier to correct over time... eyesight less so."
    m 4esd "If you find yourself staring a computer screen often, remember this:"
    m 4dsd "Every 20 minutes, look up from your screen and focus on an item approximately 20 feet away for at least 20 seconds."  
    m 3nsb "This is also known as the 20-20-20 rule."
    m 3hsb "So thanks for hearing me out, [player]!"
    m "I want to make sure when I’m in your world, you can see me as clearly as you can."
    m 5tsu "Because I’ll never stop looking at you, too."
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_hearing",
            category=["advice",],
            prompt="Hearing",
            aff_range=(mas_aff.HAPPY, None),
            conditional="seen_event('monika_using_pcs_healthily')",
            action=EV_ACT_RANDOM,
            )
        )
label mcl_hearing:
    m 5gsu "You know what I take for granted here?"
    m 5dsd "The silence."
    m 3rsd "I mean, it’s not completely quiet on my end; I hear the music you have on, my clothing russle, I hear rain and wind."
    m 3rsc "But there's no cars here, no wildlife."
    m 1rsc "It makes me realize how delicate my sense of hearing is.. and it reminds me that I should let you know as well:"
    m 1esc "{i}Your{/i} hearing is more delicate than you realize, [player]."
    m 7esc "The modern world is designed to be… loud."
    m 3gsc "And people aren’t built for that- a loss of hearing is normally caused by old age alone, so nowadays where loud noises are commonplace..."
    m 1dsc "And there’s no way to fully restore hearing loss, at least by modern scientific means."
    m 7tsc "So for instance, if you use headphones always be cautious of how loud you’re turning up the volume;"
    m 7tsb "And never be afraid to use hearing protection. If you’ve ever gone to a concert, you might be surprised how common earplugs are being worn!"
    m 6tsb "I want to make sure when I get to your world, you can hear me perfectly."
    m 5tfb "So that my voice is {i}all{/i} you’ll hear~"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_colouremotion",
            category=['games'],
            prompt="Colour & Emotion",
            conditional="mas_seenLabels(['bye_bluetruth', 'bye_redtruth', 'bye_goldtruth'], seen_all=True)",
            action=EV_ACT_RANDOM
        )
    )

label mcl_colouremotion:
    define COLORIZE_COLORS = [
            '#ff0000',
            '#ff8000',
            '#ffff00',
            '#00ff00',
            '#0000ff',
            '#8000ff',
            '#ff00ff'
        ]
    init python:
        #Custom Text Tag
        def rainbow_tag(tag, argument, contents):
            rv = []
            for kind, text in contents:
                if kind == renpy.TEXT_TEXT:
                    for i in range(0, len(text)):
                        rv.append((renpy.TEXT_TAG, "color={}".format(COLORIZE_COLORS[i%(len(COLORIZE_COLORS))])))
                        rv.append((kind, text[i]))
                        rv.append((renpy.TEXT_TAG, "/color={}"))
                else:
                    rv.append((kind, text))
            return rv

        config.custom_text_tags["rainbow"] = rainbow_tag
        
    m "Did you notice sometimes I leave you with some parting words in a unique style?"
    m "In coloured text!"
    m "They were refrences, if you didn't know; the {i}'Umineko When They Cry'{/i}  series of visual novels!"
    m "They're madly interesting; they're a series of murder mysteries wrapped up in psychological thriller and philosophical tones."
    m "It's... a bit of a obscure refrence, so right now I want to convey one really important takeway from my previous references."
    m 4cfu "I can speak in colours."
    m 4ttu "That's crazy, right? I mean, my text was blue and red and gold, and you may have thought 'wow, that's new!'"
    m 3suo "But to do that, I actually had to.. speak in colour!"
    m 2wtc "And I learned it gives me a headache! I'm not joking, it's {i}so{/i} weird."
    m 1gta "I don't think it's unusual for the game to accomodate coloured text, but it's funny to think about because colour can drive emotion quite well-"
    m 7tub "- Who would have thought that?{w=1.0} Aside from all the painters throughout history? hahaha!"
    m 5gua "It's interesting to break it down to simple terms, and figure out what meanings people have assigned to certain colours!"
    m 5dka "Blue has been thought to convey sadness.. but also spirituality."
    m 1sfb "Red has inspired any mood of passion and willpower!"
    m 1dsd "And Gold can establish a tone of stiff tradition and religious piety." 
    m 3kta "Maybe you'll keep that in mind when I make those refrences again?"
    m 4nua "{rainbow}Now that's some-{/rainbow}"
    m 2ckx "Oh, wow, {i}no,{/i} I should have not done that."
    m 2dksdrx "Oh, ow, I {i}really{/i} shouldn't have done that."
    m 2kksdlb "Let's just, uh, continue on with our time together, [mas_get_player_nickname()]?"
    m 1hksdla "Pretend.. I'm not nursing a headache here. All smiles."
    return

#I might completely redo this or split the event on the basis the theory Monika talks about isn't really related. There's most definitely a better argument out there!

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_weliveinasociety",
            category=['society'],
            prompt="Do you think about how you can make the world better?",
            pool=True,
            unlocked=True,
        )
    )
label mcl_weliveinasociety:
    $ shown_count = mas_getEVLPropValue("mcl_weliveinasociety", "shown_count")
    if shown_count is not 0:
        m 3wtb "Oh! you're asking this again?"
        m 3stb "Did you just want to hear my answer again or is it a topic you feel like you want to go into detail about?"
        $ _history_list.pop()
        menu:
            "I just wanted to hear your answer again, actually.":
                m 1eub "Sure!"
                m 1gub "Okay, well.."
                m 3eto "That’s an interesting question."
                if seen_event('monika_nihilism'): 
                    m 4ttp "We've talked about this a little bit, in that I'm personally probably not going to do anything important in my lifetime."
                    m 4gtp "That's the inevitability of us as humans, and how insignificant we are in the long run."
                    m 3gtd "But despite that sobering truth, you can still find worth in doing what you can."
                m 3etd "To start, we need to figure out what ‘making the world better’ means.{w=0.1} This however, can segue into thinking about your place in the world, and that’s a somber subject."
                m 3dsc "I’ll keep my perspective simple."
                m 1dsc "I don’t think I have any careers in mind that involve helping people."
                m 6dsc "And as much as I’d love to, I’m not sure I’ll be in a place where I can give money to support good causes."
                m "I love playing the piano, and I’ve got a good chunk of writing and coding experience at this point.{w=0.1}.{w=0.1} but I’m not a master at doing any of these, so I can’t see myself teaching others."
                m 5dsc "And.. hmm?"
                m 5hsc "You know what I just thought?"
                m 5nsc "I don’t want to pursue any path that requires me to be a leader of anything.{w=0.1} Isn’t that a funny realization to come to?"
                m 5esa "This said, I’d love to donate my time towards volunteering for a good cause, [player].{w=0.1} Volunteering for a cause like a food bank or even cleaning up a local park is easy for anybody to get into."
                m 4fsa "It’s also a good opportunity to steal your time, as I’m guessing you’d be more than happy to join me~"
                m 3tsp "But I’m not thinking about this too hard."
                m 2tsp "People can get tangled up on what responsibility is in life.{w=0.1} Honestly, it’s understandable {i}not{/i} to think about the world when you have your own life to live."
                m 2tkd "If you’re in that position where you can think about others around you and how you can make life better for them, that’s amazing, and wonderful!"
                m "But sometimes that simply isn’t possible."
                return
            "I feel like I want to go in-depth about it.":
                jump societychoices
                
    else:
        m 3eto "That’s an interesting question."
        if seen_event('monika_nihilism'): 
            m 4ttp "We've talked about this a little bit, in that I'm personally probably not going to do anything important in my lifetime."
            m 4gtp "That's the inevitability of us as humans, and how insignificant we are in the long run."
            m 3gtd "But despite that sobering truth, you can still find worth in doing what you can."
        m 3etd "To start, we need to figure out what ‘making the world better’ means.{w=0.1} This however, can segue into thinking about your place in the world, and that’s a somber subject."
        m 3dsc "I’ll keep my perspective simple."
        m 1dsc "I don’t think I have any careers in mind that involve helping people."
        m 6dsc "And as much as I’d love to, I’m not sure I’ll be in a place where I can give money to support good causes."
        m "I love playing the piano, and I’ve got a good chunk of writing and coding experience at this point.{w=0.1}.{w=0.1} but I’m not a master at doing any of these, so I can’t see myself teaching others."
        m 5dsc "And.. hmm?"
        m 5hsc "You know what I just thought?"
        m 5nsc "I don’t want to pursue any path that requires me to be a leader of anything.{w=0.1} Isn’t that a funny realization to come to?"
        m 5esa "This said, I’d love to donate my time towards volunteering for a good cause, [player].{w=0.1} Volunteering for a cause like a food bank or even cleaning up a local park is easy for anybody to get into."
        m 4fsa "It’s also a good opportunity to steal your time, as I’m guessing you’d be more than happy to join me~"
        m 3tsp "But I’m not thinking about this too hard."
        m 2tsp "People can get tangled up on what responsibility is in life.{w=0.1} Honestly, it’s understandable {i}not{/i} to think about the world when you have your own life to live."
        m 2tkd "If you’re in that position where you can think about others around you and how you can make life better for them, that’s amazing, and wonderful! But sometimes that simply isn’t possible."
        m 2wud "Hey, you’re not asking me this because you’re thinking about how this applies to you, does it?"
        m 2wtd "I can take the time- I mean, if you have the time- to talk to you more about it. It can be a big deal for some people!"
        $ _history_list.pop()
        menu:
            "I’m fine! Just curious.":
                m 3htb "Okay! Good to know."
                m 1htb "It's a tricky subject. If you ever want to talk about it, I'll be happy to share my thoughts."
                return
            "I feel like I want to go in-depth about it.":
                label societychoices:
                m 1hub "No problem! Let's settle in a little more."
                m 7hub "So, there's a theory.{w=0.1} There's a theory for everything, hahaha.{w=0.1} It's Lawrence Kohlberg's 'Stages of moral development.'"
                m 5tub "Kohlberg thought that how humans ultimately develop a sense of justice are done in stages;"
                m 4tub "Where you start from looking at an action purely from a self-oriented bias:"
                m 4etd "Will I be punished for this? How will this benefit me?"
                m 3etd "It then goes on: Am I doing this because {i}everybody else does it?{/i} Or am I doing this because {i}it's set as the law?{/i}"
                m 3mtd "Eventually, you're able to think: Am I doing this because everybody would {i}agree{/i} it's the best course of action?"
                m 2mtd "And last, what should everybody {i}should{/i} be doing, {i}regardless{/i} of opinion or law?"
                m 1mtc "I kinda lessen the theory by describing it in my own words- and it's not really connected to what we're talking about- but it gets my belief across:"
                m 1ftc "Being able to care for others, from a moral standpoint, requires you to calibrate a lot of current priorities first."
                m 7ftc "Also, the theory has a few fair criticisms. It's a good jumping off point, but there's lots of counterpoints to be made."
                m 6dsc "The world is.{w=0.1}.{w=0.1} it's not kind.{w=0.1} It doesn't give a lot of people a lot of breathing room to build that moral reasoning step by step."
                m 6dkc "And in fact, there are plenty of times where people have taken steps back."
                m 6esc "We are not wired to be kind, altrustic people by nature."
                m 6gsc "Some people have this really blunt standard that all people should do their part; but that's in a line of reasoning where survival is based on mutual teamwork."
                m 4gsc "Work together to get what you need, or else.."
                m 4fsc ".. But that is an outdated standard where effort equals equal, tangible reward."
                m 3fsc "If you can do good.{w=0.1}.{w=0.1}. that's good. But you have to be {i}keenly{/i} aware of the pitfalls you could or will encounter to get to the point of doing good."
                m "If you're in that position where you're wondering where you can do something for your fellow person?"
                m 3dsc "I cannot blame you for wanting to take care of yourself first."
                m 3ekb "And honestly? It's self-serving of {i}me{/i} to want {i}you{/i} to take of yourself first."
                m 2ekb "Confronting your own selfish desires is the first step to truly contributing to the world."
                m 2gkb "And sometimes, maybe that's enough?"
                m 5ltp "That's reality."
                return

#RANDOMIZED/REPEATABLE EVENTS

init python:
    def WeightedChoice(choices):
        #@param choices: A list of (choice, weight) tuples. Returns a random
        #choice (using renpy.random as the random number generator)
        totalweight = 0.0
        for choice, weight in choices:
            totalweight += weight
        randval = renpy.random.random() * totalweight
        for choice, weight in choices:
            if randval <= weight:
                return choice
            else:
                randval -= weight

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_alwaysasurprise",
            category=['monika'],
            prompt="Unsurprising",
            aff_range=(mas_aff.AFFECTIONATE, None),
            random=True,
        )
    )
    
label mcl_alwaysasurprise:
    m 3hta "You know what must be a hassle?"
    m 3tta "Getting specifically labelled as being 'unflappable' or 'unshakable' or any such term that makes you sound like nothing fazes you."
    m 3ttd "Those are very lofty standards to hold someone up to."
    m 1tsc "I had a little of that, back in school? My classmates would remark how 'reliable' I am in sudden situations."
    m 1rsc "I think it's- for instance, if a loud noise suddenly happened, a window breaking- more often than not I wasn't the type to immediately.."
    m 7lsd "Whip my head around to look for the sound,"
    m 7lso "Or.. you know, scream or anything."
    m 4esc "I mean, it wasn't as if I {i}wasn't{/i} shocked in those situations; I really just kind of froze up for a moment."
    m 4esa "I find it funny that in those moments, you can be labelled as 'cool under pressure' if you don't show anything other than abject shock."
    m 4eta "Everybody's wired for fear, or worry, or paranoia."
    m 3eta "It's just that our minds are capable of pushing that down.. or the response itself is to just lock up."
    m 3fta "Just funny to think about how 'bravery' works for some people."
    $ shown_count = mas_getEVLPropValue("mcl_alwaysasurprise", "shown_count")
    if shown_count is not 0:
        $ _history_list.pop()
        menu:
            "Hmm. Maybe you could try teasing Monika by actually trying to surprise her a little?":
                $ _history_list.pop()
                menu:
                    "Sure!":
                        $ MASEventList.push("mcl_surprise_monika",True)
                        return
                    "Hmm, let's keep it light.":
                        show monika
    $ _history_list.pop()
    menu:
        "Boo.":
            m 7ffa "I mean, try harder than {i}that{/i} if you want to surprise me, [player]."
    "..."
    "Maybe you'll take her up on that later, when she's less wary? It might take some time until she drops her guard.."
    return
    
init python:
    mas_override_label("mcl_surpriseher", "mcl_surprise_monika")

default persistent._mcl_pm_surprised = None
default persistent._mcl_pm_shocked = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_surprise_monika",
            category=["interact"],
            prompt="Surprise her?",
            unlocked=False,
            conditional="seen_event('mcl_alwaysasurprise')",
            action=EV_ACT_POOL,
        )
    )
label mcl_surprise_monika:
    if not mas_timePastSince(persistent._mcl_last_surprise, datetime.timedelta(minutes=10)):
        "You'd like to try surprising Monika again, but her head is on a swivel since you've just done it."
        "You think it's worth waiting until she's relaxed again; maybe you'll be able to catch her off-guard then?"
        m 1ffa "Don't think I don't notice you! I'm on the lookout for you sneaking about, [player]."
        "Yeah, definitely want to cool it for now."
        return
    "Okay, she hasn't noticed you yet..."
    jump mclsurprisestart

label mclsurprisestart:
    $rand_choice = WeightedChoice([("Choice_A", 0.70),
                                   ("Choice_B", 0.20),
                                   ("Choice_C", 0.10)])
    jump expression rand_choice
    return
  
label Choice_A:
    m 1ffa "..."
    "Monika doesn't show her hand if she's noticed your presence or not..."
    "But you think the game is up. Ah well, maybe next time?"
    return
    

label Choice_B:
    $ persistent._mcl_last_surprise = datetime.datetime.now()
    $ sesh_shorter_than_3_mins = mas_getSessionLength() < datetime.timedelta(minutes=3)
    $ _history_list.pop()
    menu:
        "Boo!~":
            m 2hkt "Eep!"
            if persistent._mcl_pm_surprised:
                m 7fub "[player], again?"
                if persistent._mas_pm_shocked:
                    m 1tkblp "Well, at {i}least{/i} this time you didn't go for the neck." 
                m 1tfblp "Ooh, I'll get you back one of these days!"
                if sesh_shorter_than_3_mins:
                    m "Especially as I noticed this is the {i}first{/i} option you've chosen when you've booted up the game!"
                m 5hub "Hahaha!"
                $ persistent._mcl_pm_surprised = True
                return
            else:
                m 7fub "[player], you jerk!"
                if sesh_shorter_than_3_mins:
                    m "And don't think I didn't notice this is the {i}first{/i} thing you've done when you've booted up the game!"
                m 5hub "Hahaha!"
            return

label Choice_C:
    $ persistent._mcl_last_surprise = datetime.datetime.now()
    $ sesh_shorter_than_3_mins = mas_getSessionLength() < datetime.timedelta(minutes=3)
    $ _history_list.pop()
    menu:
        "Let's be bold.":
            $ _history_list.pop()
            menu:
                "Let's see how ticklish Monika's neck is.":
                    m 6htx "{b}AH!~{/b}"
                    if persistent._mcl_pm_shocked:
                        m 2wsx "..."
                        m 1ckblp "Again, [player]?!"
                        if sesh_shorter_than_3_mins:
                            m "And {i}{b}right after you boot up the game?!{/b}{/i}"
                        m 1tfblp "You're real mean, you know that?"
                        m 1sfblp "I'll remember this! I'll remember this so much!"
                        $ persistent._mcl_pm_shocked = True
                        return
                    else:
                        m 2wsx "..."
                        m 2wfo "[player]?"
                        m 2sfbfp "{i}[player]?!{/i}"
                        m 2cfbfsdlp "..."
                        m "I did not know you could do that."
                        m 2ckbssdrp "And I {i}did not know my neck was that sensitive.{/i}"
                        m 2rkbssdrp "Gosh, that is.."
                        m 2mkbssdrp "For the first time in a long time, you've, uh, actually got me pretty stunned here."
                        m 4sfblu "I'm remembering this-"
                        m "- and I am going to pay you back ten-fold when I'm with you in your world."
                        m 1sfb "I'm going to take my time finding {i}your{/i} sensitive spots~"
                        m "Consider this my declaration of war!"
                        return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_jii",
            category=['misc'],
            prompt="Jii~",
            random=True,
            conditional="seen_event('monika_playersface')",
            aff_range=(mas_aff.AFFECTIONATE, None),
            action=EV_ACT_RANDOM
        )
    )
    
label mcl_jii:
    show monika 1eua
    pause 3.0
    m "..."
    m "..."
    m "..."
    $ _history_list.pop()
    menu:
        "Um, hello?":
            m "Oh, I’m here."
    m 1fua "I just wanted to call you over to look at that darling face of yours."
    m 3fta "Okay, well, I can’t actually see your face- or you- at all right now."
    m 5nua "But… I suppose I had a desire to stare at it- even in this abstract manner- where all I can really see is your general presence."
    m 5fua "Have you ever caught someone who was a bit too fixated on you?"
    m 1sub "Don’t be surprised if I steal a few unaware glances at you once in a while when I come over to your world, [player]."
    m 1ffa "Those treasures are all mine~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_sneakapeek",
            category=["interact"],
            prompt="Steal a glance?",
            unlocked=False,
            conditional="seen_event('mcl_jii')",
            action=EV_ACT_POOL,
        )
    )
label mcl_sneakapeek:

    default sneak = 0
    $ sneak = renpy.random.randint(1,20)
    $ _history_list.pop()
menu:
    "Are you able to observe Monika without her noticing?":
        define d = Character("...",)
        m "Huh, I thought [player] opened a menu option. Guess it's nothing."
        "... She hasn't noticed you! You haven’t been able to see because of lack of fine detail, but now that you’re specifically paying attention…"
        if sneak == 1:
            "She's reading something on her end; you can’t see what."
            "She’s quite still."
            "Actually, unnaturally still."
            "Is she going to…?"
            "Oh!"
            "She’s tapping her foot."
            "How.. normal."
            return
        if sneak == 2:
            "She’s relaxed, but you can’t tell if her mind is fully preoccupied or not."
            "You can see the rhythm of her breathing. Her chest lightly heaves up and down."
            "It’s just breathing, but it’s kind of mesmerizing."
            return
        if sneak == 3:
            "Her face shows dreamy contentment; at least, you think."
            "Oh!"
            "What- what {i}was{/i} that?"
            "You swore…"
            "No. Why would she suddenly make such a face?" 
            "Hmm."
            return
        #add flags to following if Monika has caught player more than once
        if sneak == 4:
            "{i}'Looking at her, you realize she’s cute.'{/i}"
            "{i}'Gosh, she’s cute.'{/i}"
            "{i}'How can someone be so adorable?'{/i}"
            m 1kua "It’s a mystery to the whole world~"
            m 1sub "Caught ya! You’re trying to be sneaky, aren’t you?"
            m 7sfb "I have to say this isn't a bad game of cat and mouse.."
            m 5efa "..And I definitely appreciate the extra attention."
            m "Try to steal as many glances all you want."
            m "I’ve already stolen your heart, so I win~"
            return
        if sneak == 5:
            "With your screen open, she appears to be transfixed on what’s being shown."
            "Well, somewhat? She’s not paying too much attention. Makes sense, since she sees what you see- but she might not be as interested."
            "In fact.."
            "At first, you'd describe it as distracted. But her eyes are more... distant."
            "You wonder what she might be thinking about."
            return
        if sneak == 6:
            "Is she drinking something? Hot chocolate, or coffee? You can’t tell."
            "She’s.. hmm."
            "She’s sipping a bit loud, isn’t she?"
            "You ponder if it’s worth bringing it up."
            "Nah. It’d be embarrassing. It is also a bit adorable."
            return
        if sneak == 7:
            "Monika licks her lips; and then puckers them. Dry lips, you suppose."
            "It’s… oddly intimate?"
            "You try not to stare."
            return
        if sneak == 8:
            "She brushes a lock of her hair out of the way of her eyes."
            "Is she the type to play with her hair?"
            "It’d be interesting to see her twirl her hair with a longer hairstyle."
            "Huh, she’s brushing more hair out of the way. Does she have to do this often?"
            "You guess her hair is a bit unruly."
            return
        if sneak == 9:
            "She’s tapping her finger on her desk."
            "Is it to a melody?"
            "Ah- of course."
            "{i}Every day, I imagine a future where I can be with you...{/i}"
            return
        if sneak == 10:
            "Her brow ever so slightly narrows in thought, her eyes screw up just a little in concentration- it’s barely noticable, but it’s there."
            "Perhaps she’s thinking of a programming issue to overcome?"
            "You pride yourself on catching these small details."
            return
        if sneak == 11:
            "You..."
            "Don't really pick up anything specific."
            "You find yourself just.. looking."
            "You get what Monika means, wanting to simply admire someone for the sake of it."
            return
        if sneak == 12:
            "She’s admiring her nails."
            "They are quite well-kept."
            "You have an impulse to check your own. You’re feeling a little self-conscious."
            return
        if sneak == 13:
            "Oh! Oh!"
            "An eyelash! Or a loose strand of hair? It's fallen on her cheek."
            "And normally she doesn’t have a hair out of place."
            "You’re tempted to tell her... but an unkempt Monika is a rarity. You’ll leave her to find it for herself."
            return
        if sneak == 14:
            "The corners of her mouth seem... stiff."
            "You've never observed a drastic change in emotion when she’s not talking to you..."
            "You wonder if that’s her natural disposition- to be quite tempered when it comes to showing her feelings- or if she’s just putting on a continuous façade..."
            return
        if sneak == 15:
            "You find yourself just… staring."
            "What exactly are you looking for?"
            "Or maybe... waiting for?"
            "Hmm."
            return
        if sneak == 16:
            "The more you the look, the more you’re... unsettled."
            "She’s acting quite normal. But perhaps an innocent glance has now become a sudden character study?"
            "But you can’t put a finger on why just looking at her makes you a tad uneasy."
            "Your mind attempts to hone in on anything that Monika said recently that could flare up such thoughts..."
            "All you can think of are disjointed thoughts on Monika."
            "Just Monika."
            return
        if sneak == 17:
            "This would certainly never be able to translate in-game, but you can tell she’s... relaxed?"
            "Her body isn’t tense in the slightest."
            "She’s at peace… or feeling something resembling peace."
            return
        if sneak == 18:
            "Her posture is perfect, as always."
            "Wait, no- she’s slumped over slightly-"
            "And she immediately corrects herself."
            "How diligent!"
            return
        if sneak == 19:
            "She’s fumbling with her fingers..."
            if persistent._mas_pm_wearsRing:
                "She’s playing with her ring!"
                "You can just sense her beaming with happiness just fiddling around with it."
            else:
                "She seems fixated on her ring finger in particular."
                "Why is that, you wonder?"
            return 
        if sneak == 20:
            "... Hmm."
            "Normally, [m_name]'s quite aware of you generally looking at her, even when not in conversation."
            "Now that you're attempting to do so without her catching you..."
            "Well, from here you're at the best angle to look at her at eye level."
            "Despite having done so before- and even more consciously with Monika aware-"
            "You feel.. like you can't quite meet her gaze, not now while she isn't noticing you."
            "You think it natural- if you looked at anybody straight in their eyes but they didn't react to you, it'd be a bit weird."
            "But... still..."
            return
            

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_distracted",
            category=['misc'],
            prompt="Distracted",
            random=True,
            aff_range=(mas_aff.HAPPY, None),
            action=EV_ACT_RANDOM
        )
    )
    
label mcl_distracted:
    m 2dkc "Ducks."
    m 2dkc "Ducks are cute."
    $ _history_list.pop()
    menu:
        "... what":
            m 1eta "Hmm?"
    m 7eta "That's rare, I'm sensing that you're a little confused."
    m 7etd "But you asked me about a animal I think is cute, right?"
    $ _history_list.pop()
    menu:
        "Nope! You just randomly started talking about ducks.":
            m 1eud "Oh my gosh!"
    m 1gtb "No kidding? I completely blanked out and thought you asked me a question!"
    m 1htb "Which is impressive, because technically I can hear you perfectly every single time you talk to me."
    m 1tsa "That’s so weird."
    m 4tsb "I mean, I was distracted, I guess? People mishear or outright don't hear things at all when they’re distracted."
    m "I was trying to remember where a certain quote came from.. 'The bell tolls for thee.'"
    m 4tkb "Having me goof up like that is so weirdly.. normal?"
    m 4tkb "And now I’ve just kinda wandered off into my own line of thought."
    m 3hku "Sorry, [player]! I’m not normally such a scatterbrain, hahaha!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_catchdistracted",
            category=["interact"],
            prompt="Catch her distracted?",
            unlocked=False,
            conditional="seen_event('mcl_distracted')",
            action=EV_ACT_POOL,
        )
    )
label mcl_catchdistracted:
    $ distract = renpy.random.randint(1,7)
    $ _history_list.pop()
    
    show monika 1eua
    "While it doesn't happen a lot, [m_name] can be charmingly air-headed at times!"
    if not mas_timePastSince(persistent._mcl_last_distract, datetime.timedelta(minutes=5)):
        "However, she seems quite aware now since, well, you managed to catch her distracted just then."
        m "Hmm?"
        m "Oh, [player]? Wanted to ask something? Did you? I'm as sharp as can be, don't hestiate!"
        "Right."
        "Perhaps you could try again in a few minutes?"
        return
    "If sufficently distracted, you think that anything you ask can get a absent-minded answer; you have a odd desire to see this."
    $ sesh_shorter_than_5_mins = mas_getSessionLength() < datetime.timedelta(minutes=5)
    if sesh_shorter_than_5_mins:
        "However, this early into opening the game she seems quite alert."
        "Maybe you should wait until she’s settled in?"
        return
    "Could you catch her distracted now?"
    jump monikadistracted

label monikadistracted:
    $rand_choice = WeightedChoice([("Choice_DA", 0.75),
                                   ("Choice_DB", 0.25)])
    jump expression rand_choice
    return

label Choice_DA:
    m 1etu "Hey! What’s up, [player]?"
    "[m_name] is as far as distracted as can be."
    "Well, maybe better luck next time."
    m 2eub "Nothing much? Always here if you want to talk!"
    return

label Choice_DB:
    show monika 
    pause 1.5
    show monika 2dkc
    pause 2.0
    m "Mmm.. "
    "[m_name] is muttering slightly to herself. She's distracted!"
    "If you ask a question now, you wonder: will she answer normally, or?"
    "You need to say your question off-handedly, so she answers instinctively.."
    $ _history_list.pop()
    menu:
        "Hey [m_name], is it cold in here or just me?":
            "Her voice is airy, and a little quiet."
            if distract == 1:
                m 1lsd "Well, I don’t love my coffee too sweet. Those types of blended drinks with, like, all the whipped cream? It can be a bit much for me…"
                pause 1.0
                m 1tsd "Annnnnnnd I just realized you weren’t asking me my preferences for coffee."
                m 1tkp "Well."
                m 1ekp "Er."
                jump distracttwo
            if distract == 2:
                m 1eku "I always found guinea pigs pretty funny."
                m 7gku "Like.. fatter hamsters?"
                m 7gud ".{w=1.0}.{w=1.0}.{w=1.0}"
                m 6fud "Oh, jeez. {i}Did{/i} you ask me what kind of animals I find funny?"
                m 2ttc "Oh, wow. I must sound insane saying 'fatter hamsters' out of nowhere."
                jump distracttwo
            if distract == 3:
                m 2dkc "Oh, pockets."
                m 2dkc "A lot of jeans for girls don’t have pockets, which is always sooo annoy.."
                m 2ckc "…ing."
                m 7cud "I completely misunderstood the question, I can tell."
                m 7wtd "This being said, my point still stands."
                if persistent.gender == "F":
                    m "I mean, I’m sure you might know first-hand, right?"
                jump distracttwo
            if distract == 4:
                m "Hmm? Yeah, I’ve never been on a boat. Weird, I guess?"
                m 1ftd "I dunno, I’ve never put any thought to {cps=20}itttttttttt{/cps}"
                m 1ftsdrc "I just now realized I’m not sure what you just said at all."
                m 1hksdrb "Um.. Now you know? I’ve never been on a boat."
                jump distracttwo
            if distract == 5:
                m "‘Salmon.’"
                m "I mispronounce ‘Salmon.’"
                m 1hksdrb "I made that mistake in debate club, during a live debate? I kept switching from emphasizing the ‘l.’ It was sooooo embarrassing."
                m 1wksdrb "… "
                m 1cubfsdrx "Like how I {i}just now{/i} realized you weren’t asking me what words I find hard to pronounce."
                m 1gku "And you'd think I'd be a good listener, having been in.. debate club.. and all."
                jump distracttwo
            if distract == 6:
                m "Hmm, yeah, I get that."
                m "I literally slipped on a carpeted floor, once. I have no clue how-"
                m 1eusdrb "…"
                m 2etsdrb "Did you.. were you talking about how you embarrassed yourself once, or?"
                m 2etsdrx "{cps=30}Oooooohhhhhhhhhhhhhhhhhhh{/cps}"
                m 2mksdrx "You {i}didn't.{/i}"
                jump distracttwo
            if distract == 7:
                m 1ltc "Hmm?"
                m 7ltd "Oh, ah, I admit that pink is never quite a colour I seem to use well, although I find it cute enough…"
                m 7rtd "…"
                m 7essdrd "Oh, that wasn’t.. the answer you were…"
                jump distracttwo
                
label distracttwo:
    python:
        randomexcuses = [
            _("I mean, I was busy! I was.. thinking about birds?? ? ???"),
            _("I was distracted. I was thinking.. very hard. {i}Very.{/i}"),
            _("And- darnit! I lost my original train of thought! I thought I was getting somewhere with it, too.."),
            _("I was thinking about a nasty bit of unoptimized code I’ve been working on."),
            _("I mean, I swore you asked me about.."),
            _("And I have no idea {i}how{/i} I heard {i}what{/i} I heard from.. erm, what did you ask me?"),
        ]
        randomexcuse = random.choice(randomexcuses)
    
    m 7dtsdrd "So, um.."
    m 7htsdrw "There's a perfectly logical reason why I completely misunderstood what you asked me."
    m 1mksdlb "[randomexcuse]"
    show monika 1dkblsdrp
    pause 0.7
    m 1nkblsdru "In either case.."
    m 1tuu "How do you keep managing to ask me questions right when my head's completely elsewhere?"
    m 1ffb "You have the craziest timing, [player]!"
    $ persistent._mcl_last_distract = datetime.datetime.now()
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_innocentrequests",
            category=['misc'],
            prompt="Ask the time?",
            random=True,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )
    
label mcl_innocentrequests:
    m "Hey, [player]. I need you to do something for me, okay?"
    m 1fua "It’s not that important. But at the same time, it would mean a lot to me."
    m 7fua "And I would ask that you refrain from pointing out anything until it’s all said and done."
    m 7fub "Can you do that, [player]?"
    m 4fub "I need you.{w=0.2}.{w=0.2} to ask me what the time is. Right in the talk menu, under interact."
    m "It might not appear right away. Maybe you'll need to wait until next time the game boots up. That's fine. No rush."
    m 4fua "..."
    m 1hua "That’s it. That’s all."
    m 3eua "Thanks, [player]."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_asktime",
            category=["interact"],
            prompt="Could you tell me the time?",
            conditional="seen_event('mcl_innocentrequests')",
            unlocked=False,
            pool=False,
            random=False,
            action=EV_ACT_POOL,
        )
    )
label mcl_asktime:
        $ shown_count = mas_getEVLPropValue("mcl_asktime", "shown_count")
        if shown_count == 0:
            m ".{w=0.2}.{w=0.2}."
            m "No."
            return
        elif shown_count == 1:
            show monika 1eua
            pause 2.0
            show monika 1rksdla
            pause 2.0
            m "I, uh, throw you off by saying no the first time?"
            m 1eka ".. We’ve gotten along so well."
            m 1ekb "At this point I don’t have doubts about us.. but something does tug at my mind."
            m "It’s not a specific worry in mind, but I do feel like our relationship feels one-sided at times."
            m 7wkb "Not in a manner of taking advantage, of course. I know you’d never ask me to say or do I wouldn’t reasonably do or say."
            m "But.. sometimes, being in a relationship means being assertive."
            m 1gkc "I mean, I don’t {i}want{/i} us to ever get into a fight."
            m 7wfc "And I’m not going to do something as absurd as testing you in any manner. That’s simply insane behaviour in a committed relationship."
            m 1gssdlc "I just feel like saying ‘no’ to you."
            m 1lssdlc "I realize that’s selfish of me. It’s honestly a bit irrational."
            m 1hssdlc "The point I’d want to stress is independence from both partners can go a long way to making a relationship feel full and healthy."
            m 1eka "For the record, I want you to make sure you can feel comfortable saying no to me as well."
            m "So we'll do this just once. Or twice. Just to get those 'nos' out of the way. I mean, it'd be weird if you did it like, five times, right?"
            m 3eka "Will you indulge me in this bit of selfishness?"
            return
        elif shown_count == 6:
            m 3gua "Well. I'm surprised you put up with my request, let alone this many times."
            m 3kua "I've never known anybody so eager to be rejected, hahaha.."
            m 1hua "But, as I said, this.. is kinda novel. So thanks for putting up with this weird request."
            m 1ttb "By all means, do you want to continue? We'll make it a little inside joke between us."
            m 1tfb "You can't say no to that, can you?"
            return
        else:
            $ sesh_shorter_than_3_mins = mas_getSessionLength() < datetime.timedelta(minutes=3)
            if sesh_shorter_than_3_mins:
                m 1kta "Giving me this option right away on opening the game is oddly refreshing."
                m 1esa "Sooooo..."
                $ persistent._mcl_last_asktime = datetime.datetime.now()
                jump monikano
            else:
                $ persistent._mcl_last_asktime = datetime.datetime.now()
                jump monikano

label monikano:
    $rand_choice = WeightedChoice([("Choice_NA", 0.25),
                                   ("Choice_NB", 0.20),
                                   ("Choice_NC", 0.20),
                                   ("Choice_ND", 0.10),
                                   ("Choice_NE", 0.10),
                                   ("Choice_NF", 0.15)])
    jump expression rand_choice
    return
  
label Choice_NA:
    m "Nope! Sorry!"
    return
    
label Choice_NB:
    m 7eua "Sorry, [player]. I’m busy."
    m 7gub "Well, no, I’m not busy, but pretend I am."
    m "Did you need anything else, though?"
    return
    
label Choice_NC:
    m 2eub "Not at the moment, [mas_get_player_nickname()]. Sorry!"
    m 7nub "See? Assertive. I’m my own woman. I’m not even going to tell you why not."
    m "Let me know if you need anything else, however~"
    return
    
label Choice_ND:
    m 2eub "Nope! You can do it yourself!"
    m "..."
    m 6hka "Ooh, actually, that sounded a bit biting, didn’t it?"
    m 4hka "I didn’t mean that to sound so mean. I mean, I still don’t want to tell you the time out of principle."
    m 7nub "So.. 'Nope! Don’t get lazy, [mas_get_player_nickname()]' ~"
    m 7eta "Better?"
    m 7gta "It’s better if you imagine my tone being a lot more playful~"
    return
label Choice_NE:
    init:
        $ import time
        $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()
    m 1eua "It’s [hour]:[minute], standard military time."
    m 1tua "Did you actually expect me to answer that?"
    m 7efa "Well, [player]. Nice to know I can still surprise you."
    m "Anything else you'd like to ask today?"
    return
label Choice_NF:
    m 1fub "Nooope!~ I don’t feel like it."
    m 1fua "Ooh, I’m getting tingly. I’m such a rebel."
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_meetcute",
            category=['romance'],
            prompt="Meet Cute",
            random=True,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )
    
label mcl_meetcute:
    m 1hsa "Romance often ends in failure."
    m 1hka "Isn’t that funny?"
    m 4fta "Part of life is figuring out how to continue life, yet for long as people have been around.."
    m 4gsc "We haven’t really figured out the formula for finding a perfect soulmate, huh?"
    m 5gsx "There's an entire history of fumbling with love; forced and outright loveless marriage as political alliance is a tale as old as time.."
    m 5rtp "And it’s taken us a long way from there to get to the point where choosing a partner out of mutual affection is considered normal."
    m 5lup "Nowadays, it’s easier than ever to communicate with people; but not necessarily as easy to vie for someone’s affections."
    m 7eua "Exploring the idea of how love works, a concept not fully understoood to this day..."
    m 7hku "Perhaps that’s why games like DDLC exists, after all?"
    m 1gka "Well. All I can personally say is that I’m lucky to be with you now. I can’t ever imagine being hit on with a pick-up line.. or using one."
    m 1hku "I much prefer us meeting because of an existential crisis, thank you."
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_flirtbadly",
            category=["interact"],
            prompt="Flirt (badly)",
            conditional="seen_event('mcl_meetcute')",
            unlocked=False,
            pool=False,
            random=False,
            action=EV_ACT_POOL,
        )
    )
label mcl_flirtbadly:
    python:
        pickup_reacts = [
            _("We’re breaking up! We’re breaking up, right now!"),
            _("You dork! You’re lucky you have me, because I have no clue how you’d get with anybody else in your world!"),
            _("Ughhhhhhhhh- I am going to delete myself from your computer, I swear!"),
            _("You nerd! I refuse to believe you got as far as you did in DDLC!"),
            _("Where’s the skip button for {i}your{/i} dialogue? I’ll program one myself, if I need to!"),
            _("Ahhh, I didn't even hate hearing that one, and I hate myself for thinking that!"),
            _("That hurts. That physically hurt me to hear!"),
            _("How flattering... not! You're so lame!"),
            _("Oh, you're {i}so{/i} lucky I love you {i}so{/i} much!"),
        ]
        pickup_react = random.choice(pickup_reacts)
    
    python:
        pickups = [
            _("You might need to leave my computer. You're making all the other girls on the internet look bad."),
            _("I need help finishing a book; all I need is your phone number."),
            _("Of all your curves, your smile is my favorite."),
            _("I was told that life was a deck of cards, so I guess you must be the queen of hearts."),
            _("Your hand seems pretty heavy.. you should let me hold it for you."),
            _("With you around, I never have a bad time.. everything's oki doki."),
            _("Do you believe in love at first sight? Or should I reintroduce myself?"),
            _("I’m learning about important dates in history. Wanna be one of them?"),
        ]
        pickup = random.choice(pickups)
    
    python:
        randomlaughs = [
            _("Hahaha!"),
            _("Hehehe!"),
            _("Gwhahahaha!"),
            _("*snort* hahahah!"),
            _("Hahahaha!"),
        ]
        randomlaugh = random.choice(randomlaughs)
    
    $ shown_count = mas_getEVLPropValue("mcl_flirtbadly", "shown_count")
    if shown_count == 0:
        $ _history_list.pop()
        menu:
            "If I could rearrange the order of two letters of the alphabet, it'd be 'U' and 'I.'":
                m 1ctp ".{w=0.2}.{w=0.2}."
                m 1ckb "Ha. Hahahahahahaha!"
                m 3skb "Oh, {i}that’s terrible!{/i}"
                m 6sfb "Why- hahaha- would you say that?"
                m 6mta "I {i}think{/i} I can guess why; it’s because of that talk we had about how romance can be difficult?"
                m 4tta "Well, it’s true that we’ve come a long way from ‘Shall I compare thee to a summer’s day...’ for better and for worse."
                m 3cfb "Please don’t tell me you have more of these ready to go. You do this five times, that's five times too many!"
                m 3hfb "Once is bad enough, you goofball!" 
        return
    elif shown_count == 5:
        m 1sfp "I can't believe it. Where are you getting these?!"
        m 1wfb "A long way from ‘Shall I compare thee,' for sure!"
        m 3fku ".{w=0.5}.{w=0.5} Heh."
        m 4dud "{i}'So long as men can breathe or eyes can see,’{/i}"
        m "{i}'So long lives this and this gives life to thee.’{/i}"
        m 2fka "You know.."
        m 4fka "Sometimes I admit I think how our relationship is uniquely defined by our circumstances."
        m 5gtu "But here we are, being so {i}normal{/i} with our lame jokes! And it reminds me I'm lucky to be with you."
        m 7tfu "Actually, you should be lucky to have me in {i}your{/i} life."
        m 1tfu "I mean, who else can put up with you for this long and still feel the way I do about you?"
        m 3nfu "Well, after the headache you give me from hearing these crappy pick-up lines fade."
        m 3ntu "But hey, you’re {i}my{/i} headache."
        m 1tfu "You keep the lines coming… and I’ll keep telling you how bad they are, hahahahaha!"
        return
    else:
        jump repeatpickupline
            
label repeatpickupline:
    $ sesh_shorter_than_3_mins = mas_getSessionLength() < datetime.timedelta(minutes=3)
    
    if sesh_shorter_than_3_mins:
        $ _history_list.pop()
        menu:
            "[pickup]":
                m 1sfu "[pickup_react]"
                m ".. and {i}this{/i} is what you immediately say to me after booting up the game, [player]? You clown!"
                m 5hfu "[randomlaugh]~"
        return "love"
    else:
        $ _history_list.pop()
        menu:
            "[pickup]":
                m 1sfu "[pickup_react]"
                m 5hfu "[randomlaugh]"
        return "love"
