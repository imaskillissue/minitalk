/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Server.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ekarpawi <ekarpawi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/15 16:35:53 by ekarpawi          #+#    #+#             */
/*   Updated: 2023/12/15 16:35:53 by ekarpawi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft/libft.h"
#include <signal.h>
#include "server.h"

t_all_the_garbage	g_;

int	handle(char c)
{
	g_.current_char = assign_bit(g_.current_char, g_.bit_index, c);
	if (g_.current_char == 0 && g_.bit_index == 8)
		return (ft_printf("\n"));
	if (++g_.bit_index == 8)
	{
		ft_printf("%c", g_.current_char);
		g_.bit_index = 0;
		g_.current_char = 0;
	}
	return (0);
}

void	handle_sigusr1(int sig)
{
	(void)sig;
	handle(1);
}

void	handle_sigusr2(int sig)
{
	(void)sig;
	handle(0);
}

int	main(void)
{
	g_ = (t_all_the_garbage){0};
	ft_printf("PID: %d\n", getpid());
	signal(SIGUSR1, handle_sigusr1);
	signal(SIGUSR2, handle_sigusr2);
	while (1)
		;
	return (0);
}
