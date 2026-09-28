"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { getAccessToken } from "@/lib/api/client";
import { getCurrentUser, UserResponse } from "@/lib/api/user";
import { logoutUser } from "@/lib/api/auth";

export default function DashboardPage() {
  const router = useRouter();
  const [user, setUser] = useState<UserResponse | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!getAccessToken()) {
      router.push("/login");
      return;
    }

    getCurrentUser()
      .then(setUser)
      .catch(() => setError("Could not load your profile. Please sign in again."))
      .finally(() => setIsLoading(false));
  }, [router]);

  const handleLogout = () => {
    logoutUser();
    router.push("/login");
  };

  if (isLoading) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <p className="text-muted-foreground">Loading your dashboard...</p>
      </div>
    );
  }

  if (error || !user) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <p className="text-destructive">{error ?? "Something went wrong."}</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-muted/40 p-6">
      <div className="mx-auto max-w-5xl space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold">Welcome back, {user.name}</h1>
            <p className="text-sm text-muted-foreground">{user.email}</p>
          </div>
          <Button variant="outline" onClick={handleLogout}>
            Log out
          </Button>
        </div>

        {/* Metric cards — placeholders until Agent 1 / Agent 2 wire real data */}
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="text-sm font-medium text-muted-foreground">Target Role</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-lg font-semibold text-muted-foreground">Not set yet</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="text-sm font-medium text-muted-foreground">Goal Target Date</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-lg font-semibold text-muted-foreground">Not set yet</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="text-sm font-medium text-muted-foreground">Overall Match Score</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-lg font-semibold text-muted-foreground">—</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="text-sm font-medium text-muted-foreground">Resume</CardTitle>
            </CardHeader>
            <CardContent>
              <Button size="sm" variant="secondary" disabled>
                Download (unavailable)
              </Button>
            </CardContent>
          </Card>
        </div>

        {/* SkillGapHeatmap and DailyPlanTimeline will slot in below once Agent 1/2 are wired */}
        <div className="rounded-lg border border-dashed p-8 text-center text-sm text-muted-foreground">
          Skill gap analysis and daily planner will appear here once you run an analysis.
        </div>
      </div>
    </div>
  );
}