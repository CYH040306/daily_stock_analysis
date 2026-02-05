# -*- coding: utf-8 -*-
"""
===================================
API v1 Schemas 模块初始化
===================================

职责：
1. 导出所有 Pydantic 模型
"""

from api.v1.schemas.common import (
    RootResponse,
    HealthResponse,
    ErrorResponse,
    SuccessResponse,
)
from api.v1.schemas.analysis import (
    AnalyzeRequest,
    AnalysisResultResponse,
    TaskAccepted,
    TaskStatus,
)
from api.v1.schemas.history import (
    HistoryItem,
    HistoryListResponse,
    NewsIntelItem,
    NewsIntelResponse,
    AnalysisReport,
    ReportMeta,
    ReportSummary,
    ReportStrategy,
    ReportDetails,
)
from api.v1.schemas.stocks import (
    StockQuote,
    StockHistoryResponse,
    KLineData,
)

__all__ = [
    # common
    "RootResponse",
    "HealthResponse",
    "ErrorResponse",
    "SuccessResponse",
    # analysis
    "AnalyzeRequest",
    "AnalysisResultResponse",
    "TaskAccepted",
    "TaskStatus",
    # history
    "HistoryItem",
    "HistoryListResponse",
    "NewsIntelItem",
    "NewsIntelResponse",
    "AnalysisReport",
    "ReportMeta",
    "ReportSummary",
    "ReportStrategy",
    "ReportDetails",
    # stocks
    "StockQuote",
    "StockHistoryResponse",
    "KLineData",
]
