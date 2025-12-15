# Based on https://gist.github.com/lutoma/9fabc3d814b82135106873423902cef4

year = ARGV[0].to_i

AnnualReport.prepare(year)

User.joins(account: :account_stat)
    .confirmed
    .merge(Account.without_suspended)
    .includes(:account)
    .where(current_sign_in_at: (Date.new(year, 1, 1)..))
    .where(account_stats: { followers_count: (1..) }).find_each do |user|
  annual_report = AnnualReport.new(user.account, year).generate

  next if annual_report.nil? || annual_report.data['top_statuses'].values.all?(&:nil?) || annual_report.data['top_hashtags'].empty?

  NotifyService.new.call(user.account, :annual_report, annual_report)
end
