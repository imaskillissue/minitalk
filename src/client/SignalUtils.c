/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   SignalUtils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ekarpawi <ekarpawi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/15 16:35:53 by ekarpawi          #+#    #+#             */
/*   Updated: 2023/12/15 16:35:53 by ekarpawi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <signal.h>
#include "client.h"

void	send_message(int pid, char *message)
{
	while (*message)
		send_char(pid, *message++);
	send_char(pid, '\n');
}

void	send_char(int pid, char c)
{
	int	i;

	i = -1;
	while (++i < 8)
	{
		if (c & (1 << i))
			kill(pid, SIGUSR1);
		else
			kill(pid, SIGUSR2);
		usleep(100);
	}
}
