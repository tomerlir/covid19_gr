from covid19_gr.statusupdatebot import StatusUpdateBot
from covid19_gr.searchbot import SearchBot
from covid19_gr.replybot import ReplyBot

rb = ReplyBot()
# sub = StatusUpdateBot()
sb = SearchBot()

sb.searchBot()
rb.reply()
# sub.updateStatus()

