"use client";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { CheckCircle2, XCircle } from "lucide-react";
import { cn } from "@/lib/utils";

interface KeywordMatch {
  keyword: string;
  category: "hard_skill" | "soft_skill";
  present_in_resume: boolean;
}

interface SkillGapHeatmapProps {
  matchPercentage: number;
  presentKeywords: KeywordMatch[];
  missingKeywords: KeywordMatch[];
}

function matchColor(pct: number): string {
  if (pct >= 75) return "text-emerald-600";
  if (pct >= 50) return "text-amber-600";
  return "text-red-600";
}

function KeywordBadge({ item, variant }: { item: KeywordMatch; variant: "present" | "missing" }) {
  const isPresent = variant === "present";
  return (
    <Badge
      variant="outline"
      className={cn(
        "gap-1.5 py-1 px-2.5 text-xs font-medium",
        isPresent
          ? "border-emerald-200 bg-emerald-50 text-emerald-700"
          : "border-red-200 bg-red-50 text-red-700"
      )}
    >
      {isPresent ? <CheckCircle2 className="h-3 w-3" /> : <XCircle className="h-3 w-3" />}
      {item.keyword}
      <span className="text-[10px] opacity-60">
        {item.category === "hard_skill" ? "hard" : "soft"}
      </span>
    </Badge>
  );
}

export function SkillGapHeatmap({ matchPercentage, presentKeywords, missingKeywords }: SkillGapHeatmapProps) {
  return (
    <Card>
      <CardHeader className="pb-3">
        <div className="flex items-center justify-between">
          <CardTitle className="text-base font-semibold">ATS Match Score</CardTitle>
          <span className={cn("text-2xl font-bold", matchColor(matchPercentage))}>
            {Math.round(matchPercentage)}%
          </span>
        </div>
        <Progress value={matchPercentage} className="h-2" />
      </CardHeader>
      <CardContent className="space-y-4">
        <div>
          <p className="mb-2 text-sm font-medium text-muted-foreground">
            Present ({presentKeywords.length})
          </p>
          <div className="flex flex-wrap gap-2">
            {presentKeywords.length > 0 ? (
              presentKeywords.map((kw) => <KeywordBadge key={kw.keyword} item={kw} variant="present" />)
            ) : (
              <p className="text-xs text-muted-foreground italic">No matching keywords yet</p>
            )}
          </div>
        </div>

        <div>
          <p className="mb-2 text-sm font-medium text-muted-foreground">
            Missing ({missingKeywords.length})
          </p>
          <div className="flex flex-wrap gap-2">
            {missingKeywords.length > 0 ? (
              missingKeywords.map((kw) => <KeywordBadge key={kw.keyword} item={kw} variant="missing" />)
            ) : (
              <p className="text-xs text-muted-foreground italic">Great — no gaps detected</p>
            )}
          </div>
        </div>
      </CardContent>
    </Card>
  );
}