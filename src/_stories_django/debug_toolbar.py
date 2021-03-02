from debug_toolbar.panels import Panel

import _stories.context
import _stories.mounted


origin_make_context = _stories.context.make_context


def track_context(storage):
    def wrapper(contract, kwargs, history):
        ctx, ns, lines, bind = origin_make_context(contract, kwargs, history)
        storage.append(ctx)
        return ctx, ns, lines, bind

    return wrapper


class StoriesPanel(Panel):
    template = "debug_toolbar/panels/stories.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.storage = []

    @property
    def nav_title(self):
        return "Stories"

    @property
    def nav_subtitle(self):
        count = len(self.storage)
        suffix = "call" if count == 1 else "calls"
        return f"{count} {suffix}"

    @property
    def title(self):
        count = len(self.storage)
        suffix = "story" if count == 1 else "stories"
        return f"Context and execution path of {count} {suffix}"

    def enable_instrumentation(self):
        _stories.mounted.make_context = track_context(self.storage)

    def disable_instrumentation(self):
        _stories.mounted.make_context = origin_make_context

    def generate_stats(self, request, response):
        self.record_stats({"stories": self.storage})
